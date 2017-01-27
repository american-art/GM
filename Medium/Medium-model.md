# Medium.csv

## Add Column
#### _MediumURI_
From column: _ObjectID_
<br/>Value: ``

#### _ObjectURI_
From column: _ObjectID_
<br/>Value: ``


## Add Node/Literal

## PyTransforms
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


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Medium_ | `skos:prefLabel` | `crm:E57_Material1`|
| _MediumURI_ | `uri` | `crm:E57_Material1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E22_Man-Made_Object1` | `crm:P45_consists_of` | `crm:E57_Material1`|
