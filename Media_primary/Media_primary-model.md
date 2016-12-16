# Media_primary.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300055547`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


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
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300055547`|
| `crm:E38_Image1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
