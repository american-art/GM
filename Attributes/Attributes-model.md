# Attributes.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _ObjectURI_
From column: _ObjectID_
``` python
return "object/"+getValue("ObjectID")
```

#### _SubjectLabel_
From column: _SourceTermID_
``` python
return "http://vocab.getty.edu/aat/"+getValue("SourceTermID")
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _SubjectLabel_ | `uri` | `owl:Thing1`|
| _Term_ | `rdfs:label` | `owl:Thing1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E22_Man-Made_Object1` | `crm:P62_depicts` | `owl:Thing1`|
