# Constituents.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404672`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/ulan`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300379842`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ConstituentURI_
From column: _AlphaSort_
``` python
return "constituent/"+SM.fingerprint_string(getValue("DisplayName"))
```

#### _NameValue_
From column: _DisplayName_
``` python
return getValue("DisplayName")
```

#### _UlanURI_
From column: _DisplayOrder_
``` python
if getValue("Creator ULAN"):
    return "http://vocab.getty.edu/ulan/"+getValue("Creator ULAN")
```

#### _InstitutionNationality_
From column: _Nationality_
``` python
if getValue("Nationality"):
    return getValue("Nationality")
else:
    return ""
```

#### _NationalityURI_
From column: _DisplayDate_
``` python
if getValue("Nationality"):
    return getValue("ConstituentURI")+"/nationality"
```

#### _AlphasortURI_
From column: _ObjectID_
``` python
return getValue("ConstituentURI")+"/alphasort"
```

#### _NameURI_
From column: _DisplayName_
``` python
return getValue("ConstituentURI")+"/name"
```

#### _BirthURI_
From column: _Institution_
``` python
if getValue("Birth Date")!='0':
    return getValue("ConstituentURI")+"/birth"
```

#### _BirthDateURI_
From column: _BirthURI_
``` python
if getValue("Birth Date")!=0:
    return getValue("ConstituentURI")+"/birth_date"
```

#### _DeathURI_
From column: _Birth Date_
``` python
if getValue("Death Date")!='0':
    return getValue("ConstituentURI")+"/death"
else:
    return ""
```

#### _DeathDateURI_
From column: _DeathURI_
``` python
if getValue("Death Date")!=0:
    return getValue("ConstituentURI")+"/death_date"
else:
    return ""
```

#### _BirthDateEnd_
From column: _Birth Date_
``` python
return getValue("Birth Date")
```

#### _BirthDisplayDate_
From column: _BirthDateEnd_
``` python
return getValue("DisplayDate")
```

#### _DeathDateEnd_
From column: _Death Date_
``` python
return getValue("Death Date")
```


## Selections
#### _DEFAULT_TEST_
From column: _LastName_
<br>Operation: `Union`
``` python
return getValue("FirstName")!=""
```


## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AlphaSort_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _AlphasortURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _Birth Date_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _BirthDateEnd_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _BirthDateURI_ | `uri` | `crm:E52_Time-Span1`|
| _BirthDisplayDate_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _ConstituentURI_ | `uri` | `crm:E39_Actor1`|
| _Death Date_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span2`|
| _DeathDateEnd_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span2`|
| _DeathDateURI_ | `uri` | `crm:E52_Time-Span2`|
| _DeathURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _DisplayDate_ | `rdfs:label` | `crm:E52_Time-Span2`|
| _DisplayName_ | `rdf:value` | `crm:E18_Physical_Thing1`|
| _DisplayName_ | `rdfs:label` | `crm:E39_Actor1`|
| _NameURI_ | `uri` | `crm:E82_Actor_Appellation2`|
| _NameValue_ | `rdf:value` | `crm:E82_Actor_Appellation2`|
| _Nationality_ | `rdfs:label` | `crm:E74_Group1`|
| _NationalityURI_ | `uri` | `crm:E74_Group1`|
| _UlanURI_ | `uri` | `skos:Concept1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation2`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E39_Actor1` | `skos:exactMatch` | `skos:Concept1`|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E39_Actor1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404672`|
| `crm:E82_Actor_Appellation2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `skos:Concept1` | `skos:inScheme` | `http://vocab.getty.edu/ulan`|
