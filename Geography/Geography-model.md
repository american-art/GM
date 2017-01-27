# Geography.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300387565`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300387567`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectURI_
From column: _ObjectID_
``` python
return "object/"+getValue("ObjectID")
```

#### _ProductionURI_
From column: _ObjectURI_
``` python
return getValue("ObjectURI")+"/production"
```

#### _PlaceURI_
From column: _ProductionURI_
``` python
return getValue("ObjectURI")+"/creation_location"
```

#### _LatURI_
From column: _LatitudeDirection_
``` python
if getValue("Latitude"):
    return getValue("ObjectURI")+"/latitude"
```

#### _LongURI_
From column: _LatURI_
``` python
if getValue("Longitude"):
    return getValue("ObjectURI")+"/longitude"
```

#### _Lat_
From column: _LatitudeDirection_
``` python
def format_latLong(str):
    deg = u"\u00b0"  # utf code for degree
    dim = str.split(' ')
    if len(dim) == 2:
        return dim[0].lstrip('0') + deg + dim[1] + "\'"
    else:
        return ""
lat = getValue("Latitude")
latDir = getValue("LatitudeDirection")
if latDir == "" or lat == "":
    return ""
else:
    return "\"" + format_latLong(lat)  + " " + latDir + " " + "\""
```

#### _Long_
From column: _LongURI_
``` python
def format_latLong(str):
    deg = u"\u00b0"  # utf code for degree
    dim = str.split(' ')
    if len(dim) == 2:
        return dim[0].lstrip('0') + deg + dim[1] + "\'"
    else:
        return ""
lng = getValue("Longitude")
lngDir = getValue("LongitudeDirection")
if lngDir == "" or lng == "":
    return ""
else:
    return "\"" + format_latLong(lng)  + " " + lngDir + " " + "\""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Lat_ | `rdf:value` | `crm:E47_Spatial_Coordinates1`|
| _LatURI_ | `uri` | `crm:E47_Spatial_Coordinates1`|
| _Long_ | `rdf:value` | `crm:E47_Spatial_Coordinates2`|
| _LongURI_ | `uri` | `crm:E47_Spatial_Coordinates2`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _PlaceURI_ | `uri` | `crm:E53_Place1`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _Term_ | `rdfs:label` | `crm:E53_Place1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P7_took_place_at` | `crm:E53_Place1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E47_Spatial_Coordinates1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300387565`|
| `crm:E47_Spatial_Coordinates2` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300387567`|
| `crm:E53_Place1` | `crm:P87_is_identified_by` | `crm:E47_Spatial_Coordinates1`|
| `crm:E53_Place1` | `crm:P87_is_identified_by` | `crm:E47_Spatial_Coordinates2`|
