# Objects_clean.csv

## Add Column
#### _ObjectURI_
From column: _ObjectID_
<br/>Value: ``

#### _ObjectNumberURI_
From column: _ObjectURI_
<br/>Value: ``

#### _ObjectNameURI_
From column: _Object Number_
<br/>Value: ``

#### _ProductionURI_
From column: _ObjectName_
<br/>Value: ``

#### _TimeSpanURI_
From column: _ProductionURI_
<br/>Value: ``

#### _PeriodURI_
From column: _DateEnd_
<br/>Value: ``

#### _CultureURI_
From column: _Period_
<br/>Value: ``

#### _DescriptionURI_
From column: _Culture_
<br/>Value: ``

#### _CopyRightURI_
From column: _CreditLine_
<br/>Value: ``

#### _InscriptionURI_
From column: _Description_
<br/>Value: ``

#### _DepartmentGroupURI_
From column: _Inscribed_
<br/>Value: ``

#### _LinguisticObjectURI_
From column: _Data Date Stamp_
<br/>Value: ``

#### _ObjectURLLabel_
From column: _LinguisticObjectURI_
<br/>Value: ``

#### _URLTypeURI_
From column: _ObjectURLLabel_
<br/>Value: ``

#### _ObjectURL_
From column: _URLTypeURI_
<br/>Value: ``


## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300179869`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `false`

#### Literal Node: `http://vocab.getty.edu/aat/300263534`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `false`

#### Literal Node: `http://vocab.getty.edu/aat/300026687`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `false`


## PyTransforms
#### _ObjectURI_
From column: _ObjectURI_
``` python
return "object/"+getValue("ObjectID")
```

#### _ObjectNumberURI_
From column: _ObjectNumberURI_
``` python
return getValue("ObjectURI")+"/object_number"
```

#### _ObjectNameURI_
From column: _ObjectNameURI_
``` python
if getValue("ObjectName"):
    return UM.uri_from_fields("thesauri/type/",getValue("ObjectName"))
else:
    return ""
```

#### _ProductionURI_
From column: _ProductionURI_
``` python
return getValue("ObjectURI")+"/production"
```

#### _TimeSpanURI_
From column: _TimeSpanURI_
``` python
return getValue("ObjectURI")+"/timespan"
```

#### _PeriodURI_
From column: _PeriodURI_
``` python
if getValue("Period"):
    return UM.uri_from_fields("thesauri/period/",getValue("Period"))
else:
    return ""
```

#### _CultureURI_
From column: _CultureURI_
``` python
if getValue("Culture"):
    return UM.uri_from_fields("thesauri/culture/",getValue("Culture"))
else:
    return ""
```

#### _DescriptionURI_
From column: _DescriptionURI_
``` python
if getValue("Description"):
    return getValue("ObjectURI")+"/description"
else:
    return ""
```

#### _InscriptionURI_
From column: _InscriptionURI_
``` python
if getValue("Inscribed"):
    return getValue("ObjectURI")+"/inscription"
else:
    return ""
```

#### _DepartmentGroupURI_
From column: _DepartmentGroupURI_
``` python
if getValue("Department"):
    return UM.uri_from_fields("thesauri/department/", getValue("Department"))
else:
    return ""
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

#### _DepartmentURI_
From column: _Inscribed_
``` python
return getValue("ObjectURI")+"/department"
```

#### _CreditURI_
From column: _Department_
``` python
return getValue("ObjectURI")+"/credit_line"
```

#### _CopyRightURI_
From column: _CopyRightURI_
``` python
return getValue("ObjectURI")+"/copyright"
```

#### _ObjectURL_
From column: _ObjectURL_
``` python
if getValue("URL"):
    return getValue("URL")
else:
    return ""
```

#### _ObjectURLLabel_
From column: _ObjectURLLabel_
``` python
return getValue("ObjectURL")
```

#### _TypeAssignment_
From column: _Period_
``` python
if getValue("Culture"):
    return getValue("ObjectURI")+"/type_assignment"
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _CopyRightURI_ | `uri` | `crm:E30_Right1`|
| _Copyright_ | `crm:P3_has_note` | `crm:E30_Right1`|
| _CreditLine_ | `rdf:value` | `crm:E33_Linguistic_Object3`|
| _CreditURI_ | `uri` | `crm:E33_Linguistic_Object3`|
| _Culture_ | `rdf:value` | `crm:E55_Type2`|
| _CultureURI_ | `uri` | `crm:E55_Type2`|
| _DateBegin_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _DateEnd_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _Dated_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _Department_ | `rdfs:label` | `crm:E74_Group1`|
| _DepartmentGroupURI_ | `uri` | `crm:E74_Group1`|
| _DepartmentURI_ | `uri` | `crm:E19_Physical_Object1`|
| _Description_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _DescriptionURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _Object Number_ | `rdfs:label` | `crm:E42_Identifier1`|
| _ObjectName_ | `rdfs:label` | `crm:E55_Type1`|
| _ObjectNameURI_ | `uri` | `crm:E55_Type1`|
| _ObjectNumberURI_ | `uri` | `crm:E42_Identifier1`|
| _ObjectNumberValue_ | `rdf:value` | `crm:E42_Identifier1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _ObjectURL_ | `uri` | `foaf:Document1`|
| _ObjectURLLabel_ | `rdfs:label` | `foaf:Document1`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _TimeSpanURI_ | `uri` | `crm:E52_Time-Span1`|
| _TypeAssignment_ | `uri` | `crm:E17_Type_Assignment2`|
| _TypeAssignmentURI_ | `uri` | `crm:E17_Type_Assignment1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P14_carried_out_by` | `crm:E39_Actor1`|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type1`|
| `crm:E17_Type_Assignment1` | `crm:P21_had_general_purpose` | `xsd:http://vocab.getty.edu/aat/300179869`|
| `crm:E17_Type_Assignment2` | `crm:P42_assigned` | `crm:E55_Type2`|
| `crm:E19_Physical_Object1` | `crm:P49_has_former_or_current_keeper` | `crm:E74_Group1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment1`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment2`|
| `crm:E22_Man-Made_Object1` | `crm:P46i_forms_part_of` | `crm:E19_Physical_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P104_is_subject_to` | `crm:E30_Right1`|
| `crm:E22_Man-Made_Object1` | `crm:P129i_is_subject_of` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object3`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E33_Linguistic_Object3` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300026687`|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E74_Group1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300263534`|
