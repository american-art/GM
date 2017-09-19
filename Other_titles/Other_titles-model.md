# Titles.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _ObjectURI_
From column: _ObjectID_
``` python
if getValue("TitleType")!="Descriptive Title":
    return "object/"+getValue("ObjectID")
else:
    return ""
```

#### _TitleURI_
From column: _ObjectURI_
``` python
return UM.uri_from_fields(getValue("ObjectURI")+"/title/",getValue("Title"))
```

#### _TitleIdentifier_
From column: _TitleURI_
``` python
return getValue("TitleURI")+"/identifier"
```

#### _TitleTypeURI_
From column: _DisplayOrder_
``` python
return getValue("TitleURI")+"/title_type"
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
| _TitleType_ | `skos:prefLabel` | `crm:E55_Type1`|
| _TitleTypeURI_ | `uri` | `crm:E55_Type1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E35_Title1` | `crm:P2_has_type` | `crm:E55_Type1`|
