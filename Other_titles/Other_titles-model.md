# Titles.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404012`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectURI_
From column: _ObjectID_
``` python
return "object/"+getValue("ObjectID")
```

#### _TitleURI_
From column: _ObjectURI_
``` python
return UM.uri_from_fields("thesauri/title/",getValue("Title"))
```

#### _TitleIdentifier_
From column: _TitleURI_
``` python
return getValue("TitleURI")+"/identifier"
```


## Selections
#### _DEFAULT_TEST_
From column: _ObjectID_
<br>Operation: `Union`
``` python
return getValue("Title Type")=="Primary Title"
```

#### _DEFAULT_TEST_
From column: _ObjectID_
<br>Operation: `Union`
``` python
return getValue("TitleType")=="Primary Title"
```


## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _Title_ | `rdf:value` | `crm:E35_Title1`|
| _TitleIdentifier_ | `uri` | `crm:E42_Identifier1`|
| _TitleType_ | `skos:prefLabel` | `crm:E55_Type1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E35_Title1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E35_Title1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404012`|
