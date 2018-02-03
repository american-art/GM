# Media_primary.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _ObjectURI_
From column: _Object ID_
``` python
return "object/"+getValue("Object ID")
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _URL_ | `uri` | `crm:E38_Image1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E22_Man-Made_Object1` | `crm:P138i_has_representation` | `crm:E38_Image1`|
