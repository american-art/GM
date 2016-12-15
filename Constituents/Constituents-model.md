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
return getValue("ConstituentURI")+"/first_name"
```

#### _FirstNameType_
From column: _FirstName_
``` python
return getValue("ConstituentURI")+"/first_name"
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AlphaSort_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _AlphasortURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _ConstituentURI_ | `uri` | `crm:E39_Actor1`|
| _DisplayName_ | `rdf:value` | `crm:E82_Actor_Appellation2`|
| _DisplayNameURI_ | `uri` | `crm:E82_Actor_Appellation2`|
| _FirstName_ | `rdf:value` | `crm:E82_Actor_Appellation4`|
| _FirstNameType_ | `skos:prefLabel` | `crm:E55_Type1`|
| _NameLabel_ | `rdfs:label` | `crm:E39_Actor1`|
| _NameURI_ | `uri` | `crm:E82_Actor_Appellation3`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation2`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation3`|
| `crm:E55_Type1` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404651`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404672`|
| `crm:E82_Actor_Appellation2` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
| `crm:E82_Actor_Appellation3` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation4`|
| `crm:E82_Actor_Appellation4` | `crm:P2_has_type` | `crm:E55_Type1`|
