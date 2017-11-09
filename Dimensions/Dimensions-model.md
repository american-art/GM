# Dimensions_clean.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300266036`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectURI_
From column: _ObjectID_
``` python
return "object/"+getValue("ObjectID")
```

#### _DimensionStringURI_
From column: _Dimensions_
``` python
if getValue("Dimensions_clean"):
    return getValue("ObjectURI")+"/dimension_string"
else:
    return ""
```

#### _PartURI_
From column: _DimensionStringURI_
``` python
return getValue("ObjectURI")+"/"+getValue("Element").lower()
```

#### _DimensionURI_
From column: _Element_
``` python
if getValue("Dimension")!="0.00":
    return getValue("PartURI")+"/dimension/"+getValue("DimensionType").lower()
else:
    return ""
```

#### _TypeURI_
From column: _DimensionURI_
``` python
return "thesauri/dimension_type/"+getValue("DimensionType").lower()
```

#### _Dimensions_clean_
From column: _Dimensions_
``` python
if getValue("Dimensions"):
    return ' '.join(getValue("Dimensions").split("\n"))
else:
    return ""
```

#### _UnitLabel_
From column: _UnitLabel_
``` python
return getValue("UnitLabel")
```

#### _UnitURI_
From column: _UnitLabel_
``` python
return UM.uri_from_fields("thesauri/dimension_type/")+getValue("UnitLabel").strip()
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Dimension_ | `rdf:value` | `crm:E54_Dimension1`|
| _DimensionStringURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _DimensionType_ | `skos:prefLabel` | `crm:E55_Type1`|
| _DimensionURI_ | `uri` | `crm:E54_Dimension1`|
| _Dimensions_clean_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _Element_ | `rdfs:label` | `crm:E18_Physical_Thing1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _PartURI_ | `uri` | `crm:E18_Physical_Thing1`|
| _TypeURI_ | `uri` | `crm:E55_Type1`|
| _UnitLabel_ | `skos:prefLabel` | `crm:E58_Measurement_Unit1`|
| _UnitURI_ | `uri` | `crm:E58_Measurement_Unit1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E18_Physical_Thing1` | `crm:P43_has_dimension` | `crm:E54_Dimension1`|
| `crm:E22_Man-Made_Object1` | `crm:P46_is_composed_of` | `crm:E18_Physical_Thing1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300266036`|
| `crm:E54_Dimension1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E54_Dimension1` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit1`|
