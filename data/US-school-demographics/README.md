US School Demographics
================

# US Schools - Total Enrollment and AP Course Enrollment by Race

## Overview

### Description

The data set included in the repository is derived from the [Civil
Rights Data Collection](https://ocrdata.ed.gov/) (CRDC), a survey
administered by the US Department of Education. The CRDC describes the
survey as

> … a survey of all public schools and school districts in the United
> States. The CRDC measures student access to courses, programs, staff,
> and resources that impact education equity and opportunity for
> students. The CRDC is a longstanding and critical aspect of the
> overall enforcement and monitoring strategy used by the Office for
> Civil Rights (OCR). In addition, the CRDC is a valuable resource for
> other federal agencies, policymakers and researchers, educators and
> school officials, parents and students, and other members of the
> public who seek data on student equity and opportunity.

We’ve taken a subset of the data focused on enrollment in AP courses by
race.

### Data

All code below can be run in R from this directory. We’ll first read the
data file.

``` r
ap_by_race <- read_csv("data/school_ap_enrollment_by_race.csv")
```

The table below shows a sample of three rows of thee data corresponding
to two schools.

| state    | district                                | school                                  | ap  | type  | total | American Indian/Alaska Native | Asian | Black | Hispanic | Native Hawaiian/Pacific Islander | Two or More Races | White |
| :------- | :-------------------------------------- | :-------------------------------------- | :-- | :---- | ----: | ----------------------------: | ----: | ----: | -------: | -------------------------------: | ----------------: | ----: |
| NEW YORK | CHARTER SCHOOL FOR APPLIED TECHNOLOGIES | CHARTER SCHOOL FOR APPLIED TECHNOLOGIES | Yes | ap    |    32 |                             0 |     0 |     2 |        7 |                                0 |                 4 |    19 |
| NEW YORK | CHARTER SCHOOL FOR APPLIED TECHNOLOGIES | CHARTER SCHOOL FOR APPLIED TECHNOLOGIES | Yes | total |  2040 |                            13 |    46 |   739 |      553 |                                0 |               169 |   520 |
| OHIO     | McDonald Local                          | McDonald High School                    | No  | total |   407 |                             4 |     0 |     4 |       13 |                                0 |                 7 |   379 |

Each row provides data about a single school, either about total
enrollment or enrollment in AP courses.

| Column name                                                                                                                               | Column meaning                                                                                                                                                                      | Example Values             |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| state                                                                                                                                     | US State (uppercase)                                                                                                                                                                | `ALABAMA`                  |
| district                                                                                                                                  | School district name                                                                                                                                                                | `Al Inst Deaf And Blind`   |
| school                                                                                                                                    | School name                                                                                                                                                                         | `Alabama School For Blind` |
| ap                                                                                                                                        | Whether the school offers any AP courses                                                                                                                                            | `yes` OR `no`              |
| type                                                                                                                                      | If `total` then the next columns refer to total enrollment numbers at the school. If `ap` then the next columns refer to the number of students enrolled in at least one AP course. | `total` OR `ap`            |
| total                                                                                                                                     | Total of students all races                                                                                                                                                         | 112                        |
| American Indian/Alaska Native <br> Asian <br> Black <br> Hispanic <br> Native Hawaiian/Pacific Islander <br> Two or More Races <br> White | 7 columns each indicating number of students identifying with each of the races. Students only identify as being in one of the categories.                                          | 49                         |

### Scripts

Run all scripts from this directory.

The scripts folder has a script `clean_original.R` which can be used to
convert the data from the [original source](#source) into the data in
the `data` folder. As the original data is not included in this
repository you will have to download and unzip the data, and then you
need to change the `data_dir` variable in the script to the location
where you unzipped the data. The script uses the `tidyverse` so you will
need to run `install.packages("tidyverse")` if you have not already done
so.

The file `README.Rmd` can be used to create this readme file from the
data in the `data` folder.

## Example Analysis

In the analysis we below we investigate the racial make-up of AP
programs within each school district as compared to the district as a
whole. Specifically, for each school district we computer the proportion
of students taking at least one AP that identify as students of color
(SOC) and the proportion of all students that identify as SOC. Here we
define SOC as any students who did not identify as White. In the code
below we create a table with this data. Note, that we remove small
school districts (\<1000 students) and also those school districts where
either 0% or 100% of AP students identified as SOC.

``` r
district_percent_soc <- ap_by_race %>%
  group_by(state, district, type) %>%
  summarize(`% SOC` =100*(1- sum(White)/sum(total)), students = sum(total)) %>%
  pivot_wider(
    names_from = c("type"),
    values_from = c("% SOC", "students"),
    names_sep = " ",
    values_fill = 0
  ) %>%
  filter(`% SOC ap` %% 1 != 0, `students total` > 1000)
```

The table below shows a sample of 14 school districts. The “% SOC total”
and “% SOC ap” columns indicate the proportion of either all students or
AP student, respectivaly, who identify as SOC. The “students total” and
“students ap” represent the total number of students and the total
number of AP students, respectively, in the district. In total there are
2992 districts in this subset of the data.

| state        | district                               | % SOC total | % SOC ap | students total | students ap |
| :----------- | :------------------------------------- | :---------- | :------- | -------------: | ----------: |
| PENNSYLVANIA | Clearfield Area SD                     | 4%          | 9%       |           1088 |         123 |
| ALABAMA      | Walker County                          | 9%          | 10%      |           2314 |         256 |
| ILLINOIS     | Cons HSD 230                           | 22%         | 20%      |           7471 |        2352 |
| ILLINOIS     | East St Louis SD 189                   | 99%         | 99%      |           1621 |         233 |
| MICHIGAN     | Kenowa Hills Public Schools            | 22%         | 11%      |           1100 |         251 |
| UTAH         | BOX ELDER DISTRICT                     | 15%         | 2%       |           2595 |         724 |
| INDIANA      | Fort Wayne Community Schools           | 53%         | 39%      |           5931 |         293 |
| GEORGIA      | Cobb County                            | 59%         | 47%      |          35141 |       10914 |
| TEXAS        | NORTHWEST ISD                          | 35%         | 32%      |           6002 |        2159 |
| PENNSYLVANIA | North Penn SD                          | 35%         | 40%      |           3036 |         809 |
| NEW YORK     | NORTH TONAWANDA CITY SCHOOL DISTRICT   | 9%          | 7%       |           1139 |         211 |
| ARIZONA      | Florence Unified School District       | 47%         | 49%      |           2879 |         119 |
| MARYLAND     | Charles County Public Schools          | 71%         | 63%      |           8431 |        2237 |
| NEW JERSEY   | South Orange-Maplewood School District | 56%         | 36%      |           1886 |         561 |

The differences in the % SOC columns gives information on the degree of
segregation within each school district. If the schools were not
segregated, we would expect that the proportion of SOC students among AP
students and the proportion among all students to be relatively close as
SOC would be as likely to take AP courses as their white peers.

The figure below shows the % SOC ap plotted against the % SOC total.
Each point represents a school district and the points are colored
according to the difference in the two percentages. The size of the
points is proportional to the total number of students in the district.
The dashed line indicates the line where the percentages are equal.

Out of all districts, 78% have a lower proportion of SOC color in the
their AP courses compared to the student body. In 4% of the proportion
of SOC in AP courses is less than half than among all students.

<img src="output/percent_soc_ap_v_total-1.svg" width="100%" />

A simple linear model predicting the % SOC among students enrolled in AP
courses based on the % SOCC among all students. As the intercept is
negative and the slope is less than one this indicates that the
predicted % SOC among students enrolled in AP courses will be lower than
what one would expect under equal representation.

``` r
lm(`% SOC ap` ~ `% SOC total`, district_percent_soc)
```

    ## 
    ## Call:
    ## lm(formula = `% SOC ap` ~ `% SOC total`, data = district_percent_soc)
    ## 
    ## Coefficients:
    ##   (Intercept)  `% SOC total`  
    ##       -1.6771         0.9107

## Sources and Licenses

The original dataset was retrieved from [Civil Rights Data Collection
(CRDC) for the 2015-16 School
Year](https://www2.ed.gov/about/offices/list/ocr/docs/crdc-2015-16.html),
specifically the (large) [zip
file](https://www2.ed.gov/about/offices/list/ocr/docs/2015-16-crdc-data.zip)
containing the entire 2015-2016 CRDC.

The dataset is public-use.

In using the data, we and any users of our derived data agree to follow
the Usage Agreement below, as provided by the CRDC.

> The data are collected in an aggregated format at the school level and
> district level. The CRDC does not collect personally identifiable
> information (e.g., studentís name, social security number, date of
> birth). To help prevent the CRDC from being used to identify any
> individuals, OCR requires that all users of the CRDC data agree that
> they will:
> 
>   - Make no use of the identity of any person discovered
>     inadvertently, and advise OCR via email at <ocrdata@ed.gov> of any
>     such discovery.
>   - Not link this dataset with individually identifiable data from
>     other datasets.
> 
> By downloading or using the CRDC dataset, you signify your agreement
> to comply with the above stated requirements.
