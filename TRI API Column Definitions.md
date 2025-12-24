### TRI API Column Definitions

| Column Name                      | Description                                                             |
|------------------------------------|------------------------------------|
| `FACILITY_NAME`                  | The name of the facility reporting to TRI                               |
| `TRI_FACILITY_ID`                | A unique identifier for the facility in the TRI database                |
| `STREET_ADDRESS`                 | The street address of the facility                                      |
| `CITY_NAME`                      | The city where the facility is located                                  |
| `COUNTY_NAME`                    | The county where the facility is located                                |
| `STATE_ABBR`                     | The two-letter abbreviation for the state where the facility is located |
| `ZIP_CODE`                       | The ZIP code of the facility's location                                 |
| `PREF_LATITUDE`                  | The preferred latitude coordinate of the facility                       |
| `PREF_LONGITUDE`                 | The preferred longitude coordinate of the facility                      |
| `PARENT_CO_NAME`                 | The name of the parent company, if applicable                           |
| `INDUSTRY_SECTOR_CODE`           | A code representing the industry sector of the facility                 |
| `INDUSTRY_SECTOR`                | A description of the industry 

**Note**: The availability and exact names of these columns may vary depending on the specific TRI API endpoint and query parameters used. Always refer to the official EPA TRI documentation for the most up-to-date and comprehensive information.

### Important Considerations

1.  Not all columns may be present in every API response.
2.  Column names may have slight variations (e.g., with or without underscores).
3.  The EPA occasionally updates their API and data structure.
4.  Some columns related to chemical releases and waste management may have additional variations or breakdowns.
5.  Numeric values (like release amounts) are typically reported in pounds, but always verify the units.
6.  For coordinates (`PREF_LATITUDE` and `PREF_LONGITUDE`), be aware that these are the preferred coordinates, which may have been adjusted for accuracy or privacy reasons.