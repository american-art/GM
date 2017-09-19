# Titles.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404670`
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
return UM.uri_from_fields(getValue("ObjectURI")+"/title/",getValue("Title"))
```

#### _TitleLabel_
From column: _Title_
``` python
return getValue("Title")
```


## Selections
#### _DEFAULT_TEST_
From column: _ObjectID_
<br>Operation: `Union`
``` python
return getValue("TitleType")!="Primary Title" and getValue("TitleType")!="Descriptive Title"
```


## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _Title_ | `rdf:value` | `crm:E35_Title1`|
| _TitleLabel_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E35_Title1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
