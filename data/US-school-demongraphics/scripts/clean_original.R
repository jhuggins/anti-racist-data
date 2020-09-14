library(tidyverse)

# Change to the folder containing the files
# CRDC 2015-16 School Data Record Layout.csv
# and 
# CRDC 2015-16 School Data.csv

data_dir <- "data/Civil Rights Edu Data 2015-16/Data Files and Layouts/"
dir("")
# load the file explaining columns
sd_layout <- read_csv(str_c(data_dir,"CRDC 2015-16 School Data Record Layout.csv"))

# set the column types and only load those which we will look at here
# specifically, those related to total enrollent by race and
# enrollment in AP courses by race
col_type <- cols_only(LEA_STATE_NAME = "c", LEA_NAME = "c", SCH_NAME = "c", SCH_GRADE_G11 = "c", SCH_ENR_HI_M = "i", SCH_ENR_HI_F = "i", SCH_ENR_AM_M = "i", SCH_ENR_AM_F = "i", SCH_ENR_AS_M = "i", SCH_ENR_AS_F = "i", SCH_ENR_HP_M = "i", SCH_ENR_HP_F = "i", SCH_ENR_BL_M = "i", SCH_ENR_BL_F = "i", SCH_ENR_WH_M = "i", SCH_ENR_WH_F = "i", SCH_ENR_TR_M = "i", SCH_ENR_TR_F = "i", SCH_APENR_IND = "c", SCH_APENR_HI_M = "i", SCH_APENR_HI_F = "i", SCH_APENR_AM_M = "i", SCH_APENR_AM_F = "i", SCH_APENR_AS_M = "i", SCH_APENR_AS_F = "i", SCH_APENR_HP_M = "i", SCH_APENR_HP_F = "i", SCH_APENR_BL_M = "i", SCH_APENR_BL_F = "i", SCH_APENR_WH_M = "i", SCH_APENR_WH_F = "i", SCH_APENR_TR_M = "i", SCH_APENR_TR_F = "i")

sd_df <- read_csv(str_c(data_dir, "CRDC 2015-16 School Data.csv"), col_types = col_type)

# Only keep schools that have Grade 11 and have reported whether they have any
# AP students or not
ap <- sd_df %>%
  filter(SCH_GRADE_G11 == "Yes", SCH_APENR_IND != "-9") %>%
  select(-SCH_GRADE_G11) %>%
  pivot_longer( # Pivot data so that we can summarize by race, removing gender
    cols = c(starts_with("SCH_APENR"),-SCH_APENR_IND, starts_with("SCH_ENR")),
    names_to = "var", values_to = "val"
  ) %>%
  left_join( # Join with the description table to rename columns
    sd_layout %>% select(Field_Name, Field_Description),
    by = c("var" = "Field_Name")) %>%
  filter(val >= 0) %>%
  mutate( # extract ap/total indicator, race, and sex
    type = ifelse(str_detect(Field_Description, "AP Course"), "ap", "total"),
    race = str_extract(Field_Description, "(?<=: )(.*)(?= (Male)| (Female))"),
    sex = str_extract(Field_Description, "\\w*$")
  ) %>%
  select(-var, -Field_Description) %>%
  group_by_at(vars(LEA_STATE_NAME:SCH_APENR_IND, type, race)) %>%
  summarize(enrollment = sum(val)) %>% # add together male and femaile
  ungroup() %>%
  rename( # rename variables to be more convenient
    state = LEA_STATE_NAME,
    district = LEA_NAME,
    school = SCH_NAME,
    ap = SCH_APENR_IND)

# Pivot the table to be wider to have columns for each race
ap_by_race <- ap %>%
  group_by(state, district, school, type, ap) %>%
  mutate(total = sum(enrollment, na.rm=TRUE)) %>%
  pivot_wider(names_from = "race", values_from = "enrollment") %>%
  ungroup()

write_csv(ap_by_race, "data/school_ap_enrollment_by_race.csv")
