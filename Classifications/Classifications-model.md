# Classifications.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300179869`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ClassificationAatTerm_
From column: _Classification_
``` python
return AATTerm.get_aat_term("gm",getValue("Classification"))
```

#### _ClassificationAatURI_
From column: _ClassificationAatTerm_
``` python
return AATTerm.get_aat_uri("gm",getValue("Classification"))
```

#### _ObjectURI_
From column: _ObjectID_
``` python
return "object/"+getValue("ObjectID")
```

#### _TypeURI_
From column: _ObjectURI_
``` python
if AATTerm.get_aat_uri("gm",getValue("Classification")):
    return AATTerm.get_aat_uri("gm",getValue("Classification"))
else:
    return UM.uri_from_fields("thesauri/classification/",getValue("Classification"))
```

#### _ClassificationEventURI_
From column: _ObjectID_
``` python
return getValue("ObjectURI")+"/classification_event"
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Classification_ | `rdfs:label` | `crm:E55_Type1`|
| _ClassificationEventURI_ | `uri` | `crm:E17_Type_Assignment1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _TypeURI_ | `uri` | `crm:E55_Type1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type1`|
| `crm:E17_Type_Assignment1` | `crm:P21_had_general_purpose` | `xsd:http://vocab.getty.edu/aat/300179869`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment1`|
| `crm:E22_Man-Made_Object1` | `crm:P2_has_type` | `crm:E55_Type1`|
