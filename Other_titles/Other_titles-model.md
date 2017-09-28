# Titles.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _ObjectURI_
From column: _ObjectID_
``` python
return "object/"+getValue("ObjectID")
```

#### _TitleURI_
From column: _Title_
``` python
if getValue("DisplayOrder") != "1":
    return UM.uri_from_fields(getValue("ObjectURI")+"/title/",getValue("Title"))
else:
    return ""
```

#### _TitleTypeURI_
From column: _TitleType_
``` python
if getValue("DisplayOrder") != "1":
    return UM.uri_from_fields("thesauri/title_type/", getValue("TitleType"))
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _Title_ | `rdf:value` | `crm:E35_Title1`|
| _TitleType_ | `skos:prefLabel` | `crm:E55_Type1`|
| _TitleTypeURI_ | `rdf:value` | `crm:E55_Type1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E35_Title1` | `crm:P2_has_type` | `crm:E55_Type1`|
