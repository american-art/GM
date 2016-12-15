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

#### Literal Node: `http://vocab.getty.edu/aat/300404651`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ConstituentURI_
From column: _DisplayName_
``` python
return "object/"+SM.fingerprint_string(getValue("DisplayName"))
```

#### _NameLabel_
From column: _DisplayName_
``` python
return getValue("DisplayName")
```

#### _AlphasortURI_
From column: _ConstituentURI_
``` python
return getValue("ConstituentURI")+"/alphasort"
```

#### _DisplayNameURI_
From column: _AlphaSort_
``` python
return getValue("ConstituentURI")+"/display_name"
```

#### _NameURI_
From column: _NameLabel_
``` python
return getValue("ConstituentURI")+"/name"
```

#### _FirstName_
From column: _FirstName_
``` python
return getValue("FirstName")
```

#### _FirstNameType_
From column: _FirstName_
``` python
return "First Name"
```

#### _MiddleNameType_
From column: _MiddleName_
``` python
return "Middle Name"
```

#### _LastNameType_
From column: _LastName_
``` python
return "Last Name"
```

#### _FirstNameURI_
From column: _AlphasortURI_
``` python
return getValue("ConstituentURI")+"/first_name"
```

#### _MiddleNameURI_
From column: _FirstNameType_
``` python
return getValue("ConstituentURI")+"/middle_name"
```

#### _LastNameURI_
From column: _MiddleNameType_
``` python
return getValue("ConstituentURI")+"/last_name"
```

#### _FirstNameTypeURI_
From column: _FirstName_
``` python
return getValue("ConstituentURI")+"/first_name_type"
```

#### _MiddleNameTypeURI_
From column: _MiddleName_
``` python
return getValue("ConstituentURI")+"/middle_name_type"
```

#### _LastNameTypeURI_
From column: _LastName_
``` python
return getValue("ConstituentURI")+"/last_name_type"
```

#### _SuffixURI_
From column: _LastNameType_
``` python
if getValue("Suffix"):
    return getValue("ConstituentURI")+"/suffix"
else:
    return ""
```

#### _PrefixURI_
From column: _Suffix_
``` python
if getValue("prefix"):
    return getValue("ConstituentURI")+"/suffix"
else:
    return ""
```

#### _BiographyURI_
From column: _Prefix_
``` python
return getValue("ConstituentURI")+"/biography"
```

#### _BirthURI_
From column: _Institution_
``` python
return getValue("ConstituentURI")+"/birth"
```

#### _BirthYearURI_
From column: _BirthURI_
``` python
return getValue("ConstituentURI")+"/birth_year"
```

#### _DeathURI_
From column: _Birth Date_
``` python
return getValue("ConstituentURI")+"/death"
```

#### _DeathYearURI_
From column: _DeathURI_
``` python
return getValue("ConstituentURI")+"/death_year"
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AlphaSort_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _AlphasortURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _Biography_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _BiographyURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _Birth Date_ | `rdf:value` | `crm:E52_Time-Span1`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _BirthearURI_ | `uri` | `crm:E52_Time-Span1`|
| _ConstituentURI_ | `uri` | `crm:E39_Actor1`|
| _Death Date_ | `rdf:value` | `crm:E52_Time-Span2`|
| _DeathURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _DeathYearURI_ | `uri` | `crm:E52_Time-Span2`|
| _DisplayName_ | `rdf:value` | `crm:E82_Actor_Appellation2`|
| _DisplayNameURI_ | `uri` | `crm:E82_Actor_Appellation2`|
| _FirstName_ | `rdf:value` | `crm:E82_Actor_Appellation4`|
| _FirstNameURI_ | `uri` | `crm:E82_Actor_Appellation4`|
| _LastName_ | `rdf:value` | `crm:E82_Actor_Appellation6`|
| _LastNameURI_ | `uri` | `crm:E82_Actor_Appellation6`|
| _MiddleName_ | `rdf:value` | `crm:E82_Actor_Appellation5`|
| _MiddleNameURI_ | `uri` | `crm:E82_Actor_Appellation5`|
| _NameLabel_ | `rdfs:label` | `crm:E39_Actor1`|
| _NameURI_ | `uri` | `crm:E82_Actor_Appellation3`|
| _Prefix_ | `rdf:value` | `crm:E82_Actor_Appellation8`|
| _PrefixURI_ | `uri` | `crm:E82_Actor_Appellation8`|
| _Suffix_ | `rdf:value` | `crm:E82_Actor_Appellation7`|
| _SuffixURI_ | `uri` | `crm:E82_Actor_Appellation7`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P129i_is_subject_of` | `crm:E33_Linguistic_Object1`|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation2`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation3`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404672`|
| `crm:E82_Actor_Appellation2` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
| `crm:E82_Actor_Appellation3` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation4`|
| `crm:E82_Actor_Appellation3` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation5`|
| `crm:E82_Actor_Appellation3` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation6`|
| `crm:E82_Actor_Appellation3` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation7`|
| `crm:E82_Actor_Appellation3` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation8`|
