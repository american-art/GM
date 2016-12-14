## Medium.csv

### PyTransforms
#### _ObjectURI_
From column: _ObjectURI_
``` python
return "object/"+getValue("ObjectID")
```

#### _MediumURI_
From column: _MediumURI_
``` python
return getValue("ObjectURI")+"/medium"
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Attribution_ | `crm:P3_has_note` | `crm:E39_Actor2`|
| _AttributionURI_ | `uri` | `crm:E39_Actor2`|
| _BeginDate_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _ConTypeURI_ | `uri` | `crm:E55_Type1`|
| _ConstituentType_ | `rdfs:label` | `crm:E55_Type1`|
| _ConstituentURI_ | `uri` | `crm:E39_Actor1`|
| _CopyRightURI_ | `uri` | `crm:E30_Right1`|
| _Copyright_ | `crm:P3_has_note` | `crm:E30_Right1`|
| _Credit_ | `crm:P3_has_note` | `crm:E82_Actor_Appellation1`|
| _Culture_ | `rdfs:label` | `crm:E55_Type2`|
| _CultureURI_ | `uri` | `crm:E55_Type2`|
| _DateURI_ | `uri` | `crm:E52_Time-Span1`|
| _DateURI_ | `uri` | `crm:E49_Time_Appellation1`|
| _Dated_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _Dated_ | `rdfs:label` | `crm:E49_Time_Appellation1`|
| _Dated_ | `crm:P3_has_note` | `crm:E52_Time-Span1`|
| _Department_ | `rdfs:label` | `crm:E55_Type5`|
| _Department_ | `rdfs:label` | `crm:E55_Type3`|
| _DepartmentURI_ | `uri` | `crm:E55_Type5`|
| _Description_ | `rdfs:label` | `crm:E18_Physical_Thing1`|
| _Description_ | `crm:P3_has_note` | `crm:E33_Linguistic_Object1`|
| _DescriptionURI_ | `uri` | `crm:E18_Physical_Thing1`|
| _DescriptionURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _DimensionURI_ | `uri` | `crm:E54_Dimension1`|
| _Dimensions_ | `crm:P3_has_note` | `crm:E54_Dimension1`|
| _Display Name_ | `rdfs:label` | `crm:E82_Actor_Appellation2`|
| _DisplayDate_ | `crm:P62i_is_depicted_by` | `crm:E52_Time-Span1`|
| _DisplayNameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _DisplayNameURI_ | `uri` | `crm:E82_Actor_Appellation2`|
| _EndDate_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _FirstName_ | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation1`|
| _Image Full Size URL_ | `crm:P3_has_note` | `crm:E38_Image1`|
| _ImageURI_ | `uri` | `crm:E38_Image1`|
| _Inscribed_ | `crm:P3_has_note` | `crm:E34_Inscription1`|
| _InscriptionURI_ | `uri` | `crm:E34_Inscription1`|
| _LastName_ | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation1`|
| _LinguisticObjectURI_ | `uri` | `crm:E33_Linguistic_Object2`|
| _Media_ | `rdfs:label` | `crm:E55_Type4`|
| _MediaURI_ | `uri` | `crm:E55_Type4`|
| _Medium_ | `rdfs:label` | `crm:E55_Type1`|
| _Medium_ | `crm:P3_has_note` | `crm:E55_Type3`|
| _MediumURI_ | `uri` | `crm:E55_Type3`|
| _MediumURI_ | `uri` | `crm:E55_Type1`|
| _MiddleName_ | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation1`|
| _NameTitle_ | `crm:P102_has_title` | `crm:E82_Actor_Appellation1`|
| _Object Number_ | `rdfs:label` | `crm:E42_Identifier1`|
| _ObjectNumberURI_ | `uri` | `crm:E42_Identifier1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _Period_ | `rdfs:label` | `crm:E4_Period1`|
| _PeriodURI_ | `uri` | `crm:E4_Period1`|
| _PrimaryTitleTranslationTypeURI_ | `uri` | `crm:E55_Type6`|
| _PrimaryTitleTransltionType_ | `rdfs:label` | `crm:E55_Type6`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _Suffix_ | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation1`|
| _Title_ | `rdfs:label` | `crm:E35_Title1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|
| _URL_ | `crm:P3_has_note` | `crm:E42_Identifier2`|
| _urlURI_ | `uri` | `crm:E42_Identifier2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E22_Man-Made_Object1` | `crm:P2_has_type` | `crm:E55_Type1`|
