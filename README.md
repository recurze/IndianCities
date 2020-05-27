# IndianCities
This repository shall contain a dataset with information on population, location
and area of the main cities of India. The cities included in this dataset all
have a population of 1Lakh (100k) or more. It also includes these information on
all the districts of India.

## Data Sources

* The population data of the cities have been retreived from the [Census of
  2011][census] conducted by the Indian Government. The website also has it's
  own [consolidated list][1lcities_pdf] of cites with a population of 1Lakh and
  above.

* Latitude and Longitude of the cities were taken from https://latlong.net; for
  the cities missing from their database, information was filled in from
  [Wikipedia](https://en.wikipedia.org).

* [Villageinfo](https://villageinfo.in) was used to collect information on area
  of cities and towns, both small and large. Area for cities missing from there
  were filled in from Wikipedia again.

* There are still cities for which finding these information has been hard. One
  could go through state's or the district's website to see if it can be found.



[census]: https://censusindia.gov.in/pca/pcadata/pca.html
[1lcities_pdf]: https://www.censusindia.gov.in/2011-prov-results/paper2/data_files/India2/Table_2_PR_Cities_1Lakh_and_Above.pdf
