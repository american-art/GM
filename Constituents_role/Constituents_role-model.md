# Constituents.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _ObjectURI_
From column: _ObjectID_
``` python
if getValue("Role") in ["Artist","Author","Engraver","Original Artist","Subject"]:
    return "object/"+getValue("ObjectID")
else:
    return ""
```

#### _ArtistURI_
From column: _AlphaSort_
``` python
if getValue("Role") in ["Artist","Author","Engraver","Original Artist"]:
    return "constituent/"+SM.fingerprint_string(getValue("DisplayName"))
else:
    return ""
```

#### _AlphaSort_
From column: _AlphaSort_
``` python
return getValue("AlphaSort")
```

#### _ProductionURI_
From column: _AlphaSort_
``` python
if getValue("Role") in ["Artist","Author","Engraver","Original Artist"]:
    return getValue("ObjectURI")+"/production"
else:
    return ""
```

#### _SubjectURI_
From column: _ArtistURI_
``` python
if getValue("Role")=="Subject":
    return "constituent/"+SM.fingerprint_string(getValue("DisplayName"))
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ArtistURI_ | `uri` | `crm:E39_Actor1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _SubjectURI_ | `uri` | `crm:E39_Actor2`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P14_carried_out_by` | `crm:E39_Actor1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P62_depicts` | `crm:E39_Actor2`|
