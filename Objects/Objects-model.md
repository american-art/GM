# Objects_clean.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300179869`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300080091`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

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

#### _ObjectNumberURI_
From column: _ObjectURI_
``` python
return getValue("ObjectURI")+"/object_number"
```

#### _ObjectNumberValue_
From column: _Object Number_
``` python
return getValue("Object Number")
```

#### _TypeAssignmentURI_
From column: _ObjectNumberValue_
``` python
return getValue("ObjectURI")+"/type_assignment"
```

#### _ObjectNameURI_
From column: _TypeAssignmentURI_
``` python
if getValue("ObjectName"):
    return UM.uri_from_fields("thesauri/type/",getValue("ObjectName"))
else:
    return ""
```

#### _ProductionURI_
From column: _ObjectName_
``` python
return getValue("ObjectURI")+"/production"
```

#### _CultureTypeURI_
From column: _Period_
``` python
if getValue("Culture"):
    return getValue("ObjectURI")+"/culture_type_assignment"
else:
    return ""
```

#### _CultureURI_
From column: _CultureTypeURI_
``` python
if getValue("Culture"):
    return UM.uri_from_fields("thesauri/culture/",getValue("Culture"))
else:
    return ""
```

#### _DescriptionURI_
From column: _Culture_
``` python
if getValue("Description"):
    return getValue("ObjectURI")+"/description"
else:
    return ""
```

#### _DepartmentURI_
From column: _Inscribed_
``` python
return getValue("ObjectURI")+"/department"
```

#### _DepartmentGroupURI_
From column: _DepartmentURI_
``` python
if getValue("Department"):
    return UM.uri_from_fields("thesauri/department/", getValue("Department"))
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Culture_ | `rdf:value` | `crm:E55_Type2`|
| _CultureURI_ | `uri` | `crm:E55_Type2`|
| _Culture_Type_ | `uri` | `crm:E17_Type_Assignment2`|
| _Department_ | `rdfs:label` | `crm:E74_Group1`|
| _DepartmentGroupURI_ | `rdfs:label` | `crm:E74_Group1`|
| _DepartmentURI_ | `uri` | `crm:E19_Physical_Object1`|
| _Description_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _DescriptionURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _Object Number_ | `rdfs:label` | `crm:E42_Identifier1`|
| _ObjectName_ | `rdfs:label` | `crm:E55_Type1`|
| _ObjectNameURI_ | `uri` | `crm:E55_Type1`|
| _ObjectNumberURI_ | `uri` | `crm:E42_Identifier1`|
| _ObjectNumberValue_ | `rdf:value` | `crm:E42_Identifier1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _TypeAssignmentURI_ | `uri` | `crm:E17_Type_Assignment1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type1`|
| `crm:E17_Type_Assignment1` | `crm:P21_had_general_purpose` | `xsd:http://vocab.getty.edu/aat/300179869`|
| `crm:E17_Type_Assignment2` | `crm:P42_assigned` | `crm:E55_Type2`|
| `crm:E19_Physical_Object1` | `crm:P49_has_former_or_current_keeper` | `crm:E74_Group1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment1`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment2`|
| `crm:E22_Man-Made_Object1` | `crm:P46i_forms_part_of` | `crm:E19_Physical_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P129i_is_subject_of` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300080091`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
