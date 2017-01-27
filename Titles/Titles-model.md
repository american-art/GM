# Titles.csv

## Add Column
#### _ObjectURI_
From column: _ObjectID_
<br/>Value: ``

#### _TitleLabel_
From column: _Title_
<br/>Value: ``


## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectURI_
From column: _ObjectURI_
``` python
return "object/"+getValue("ObjectID")
```

#### _TitleLabel_
From column: _TitleLabel_
``` python
return getValue("Title")
```

#### _TitleURI_
From column: _ObjectURI_
``` python
return UM.uri_from_fields("thesauri/title/",getValue("Title"))
```


## Selections
#### _DEFAULT_TEST_
From column: _TitleType_
<br>Operation: `Union`
``` python
return getValue("TitleType")!="Primary Title"
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
| `crm:E35_Title1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
