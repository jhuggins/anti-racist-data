US School Demographics
================
Daniel Sussman
9/13/2020

US Schools - Total Enrollment and AP Course Enrollment by Race
==============================================================

Overview
--------

Description
-----------

The data set included in the repository is derived from the [Civil Rights Data Collection](https://ocrdata.ed.gov/).

> The Civil Rights Data Collection (CRDC) is a survey of all public schools and school districts in the United States. The CRDC measures student access to courses, programs, staff, and resources that impact education equity and opportunity for students. The CRDC is a longstanding and critical aspect of the overall enforcement and monitoring strategy used by the Office for Civil Rights (OCR). In addition, the CRDC is a valuable resource for other federal agencies, policymakers and researchers, educators and school officials, parents and students, and other members of the public who seek data on student equity and opportunity.

We've taken a subset of the data focused on enrollment in AP courses by race.

### Data

All code below can be run in R from this directory. We'll first read the data file.

``` r
ap_by_race <- read_csv("data/school_ap_enrollment_by_race.csv")
```

The table below shows a sample of three rows of thee data corresponding to two schools.

<table>
<colgroup>
<col width="4%" />
<col width="18%" />
<col width="18%" />
<col width="2%" />
<col width="3%" />
<col width="3%" />
<col width="13%" />
<col width="3%" />
<col width="3%" />
<col width="4%" />
<col width="15%" />
<col width="8%" />
<col width="3%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">state</th>
<th align="left">district</th>
<th align="left">school</th>
<th align="left">ap</th>
<th align="left">type</th>
<th align="right">total</th>
<th align="right">American Indian/Alaska Native</th>
<th align="right">Asian</th>
<th align="right">Black</th>
<th align="right">Hispanic</th>
<th align="right">Native Hawaiian/Pacific Islander</th>
<th align="right">Two or More Races</th>
<th align="right">White</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">NEW YORK</td>
<td align="left">CHARTER SCHOOL FOR APPLIED TECHNOLOGIES</td>
<td align="left">CHARTER SCHOOL FOR APPLIED TECHNOLOGIES</td>
<td align="left">Yes</td>
<td align="left">ap</td>
<td align="right">32</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">2</td>
<td align="right">7</td>
<td align="right">0</td>
<td align="right">4</td>
<td align="right">19</td>
</tr>
<tr class="even">
<td align="left">NEW YORK</td>
<td align="left">CHARTER SCHOOL FOR APPLIED TECHNOLOGIES</td>
<td align="left">CHARTER SCHOOL FOR APPLIED TECHNOLOGIES</td>
<td align="left">Yes</td>
<td align="left">total</td>
<td align="right">2040</td>
<td align="right">13</td>
<td align="right">46</td>
<td align="right">739</td>
<td align="right">553</td>
<td align="right">0</td>
<td align="right">169</td>
<td align="right">520</td>
</tr>
<tr class="odd">
<td align="left">OHIO</td>
<td align="left">McDonald Local</td>
<td align="left">McDonald High School</td>
<td align="left">No</td>
<td align="left">total</td>
<td align="right">407</td>
<td align="right">4</td>
<td align="right">0</td>
<td align="right">4</td>
<td align="right">13</td>
<td align="right">0</td>
<td align="right">7</td>
<td align="right">379</td>
</tr>
</tbody>
</table>

Each row provides data about a single school, either about total enrollment or enrollment in AP courses.

<table style="width:65%;">
<colgroup>
<col width="19%" />
<col width="23%" />
<col width="22%" />
</colgroup>
<thead>
<tr class="header">
<th>Column name</th>
<th>Column meaning               </th>
<th>Example Values</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>state</td>
<td>US State (uppercase)</td>
<td><code>ALABAMA</code></td>
</tr>
<tr class="even">
<td>district</td>
<td>School district name</td>
<td><code>Al Inst Deaf And Blind</code></td>
</tr>
<tr class="odd">
<td>school</td>
<td>School name</td>
<td><code>Alabama School For Blind</code></td>
</tr>
<tr class="even">
<td>ap</td>
<td>Whether the school offers any AP courses</td>
<td><code>yes</code> OR <code>no</code></td>
</tr>
<tr class="odd">
<td>type</td>
<td>If <code>total</code> then the next columns refer to total enrollment numbers at the school. If <code>ap</code> then the next columns refer to the number of students enrolled in at least one AP course.</td>
<td><code>total</code> OR <code>ap</code></td>
</tr>
<tr class="even">
<td>total</td>
<td>Total of students all races</td>
<td>112</td>
</tr>
<tr class="odd">
<td>American Indian/Alaska Native, Asian, Black, Hispanic, Native Hawaiian/Pacific Islander, Two or More Races, White</td>
<td>7 columns each indicating number of students identifying with each of the races above. Students only identify as being in one of the categories.</td>
<td>49</td>
</tr>
</tbody>
</table>

### Scripts

Run all scripts from this directory.

The scripts folder has a script `clean_original.R` which can be used to convert the data from the [original source](#source) into the data in the `data` folder. As the original data is not included in this repository you will have to download and unzip the data, and then you need to change the `data_dir` variable in the script to the location where you unzipped the data. The script uses the `tidyverse` so you will need to run `install.packages("tidyverse")` if you have not already done so.

The file `README.Rmd` can be used to create this readme file from the data in the `data` folder.

Example Analysis
----------------

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

| state        | district                               | % SOC total | % SOC ap |  students total|  students ap|
|:-------------|:---------------------------------------|:------------|:---------|---------------:|------------:|
| PENNSYLVANIA | Clearfield Area SD                     | 4%          | 9%       |            1088|          123|
| ALABAMA      | Walker County                          | 9%          | 10%      |            2314|          256|
| ILLINOIS     | Cons HSD 230                           | 22%         | 20%      |            7471|         2352|
| ILLINOIS     | East St Louis SD 189                   | 99%         | 99%      |            1621|          233|
| MICHIGAN     | Kenowa Hills Public Schools            | 22%         | 11%      |            1100|          251|
| UTAH         | BOX ELDER DISTRICT                     | 15%         | 2%       |            2595|          724|
| INDIANA      | Fort Wayne Community Schools           | 53%         | 39%      |            5931|          293|
| GEORGIA      | Cobb County                            | 59%         | 47%      |           35141|        10914|
| TEXAS        | NORTHWEST ISD                          | 35%         | 32%      |            6002|         2159|
| PENNSYLVANIA | North Penn SD                          | 35%         | 40%      |            3036|          809|
| NEW YORK     | NORTH TONAWANDA CITY SCHOOL DISTRICT   | 9%          | 7%       |            1139|          211|
| ARIZONA      | Florence Unified School District       | 47%         | 49%      |            2879|          119|
| MARYLAND     | Charles County Public Schools          | 71%         | 63%      |            8431|         2237|
| NEW JERSEY   | South Orange-Maplewood School District | 56%         | 36%      |            1886|          561|

<img src="output/percent_soc_ap_v_total-1.svg" width="100%" />

A simple linear model predicting the % SOC among students enrolled in AP courses based on the % SOCC among all students. As the intercept is negative and the slope is less than one this indicates that the predicted % SOC among students enrolled in AP courses will be lower than what one would expect under equal representation.

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

Sources and Licenses
--------------------

The original dataset was retrieved from [Civil Rights Data Collection (CRDC) for the 2015-16 School Year](https://www2.ed.gov/about/offices/list/ocr/docs/crdc-2015-16.html), specifically the (large) [zip file](https://www2.ed.gov/about/offices/list/ocr/docs/2015-16-crdc-data.zip) containing the entire 2015-2016 CRDC.

The dataset is public-use.

In using the data we any users of our derived data agree to follow the following Usage Agreement as provided by the CRDC.

> The data are collected in an aggregated format at the school level and district level. The CRDC does not collect personally identifiable information (e.g., studentís name, social security number, date of birth). To help prevent the CRDC from being used to identify any individuals, OCR requires that all users of the CRDC data agree that they will:
>
> -   Make no use of the identity of any person discovered inadvertently, and advise OCR via email at <ocrdata@ed.gov> of any such discovery.
> -   Not link this dataset with individually identifiable data from other datasets.
>
> By downloading or using the CRDC dataset, you signify your agreement to comply with the above stated requirements.
