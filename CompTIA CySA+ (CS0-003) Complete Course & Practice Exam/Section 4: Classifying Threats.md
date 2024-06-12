# Classifying Threats

## Overview

```mermaid

mindmap
  root((Classifying Threats))
    Security Operations
        Compare and contrast threat-intelligence and threat-hunting concepts
    Vulnerability Management
        Givern a scenario, you must analyse data to determine vulnerabilities
    Incident Response Management
        Explain concepts related to attack methodology frameworks
```

## Threat Classificiations

```mermaid

mindmap
  root((Threats))
    Known
        Can be identified using basic signature or pattern matching
            Malware
            Documented exploits
    Unknown
        Cannot be identified using basic signature or pattern matching
            Zero-day exploits
            Recycled threats
            Obfuscated malware code
            Behavior-based detection
            Known & Unknown unknowns

```

More on the `Known & Unknown unknowns`

```mermaid

quadrantChart
    title Known & Unknown unknowns
    quadrant-1 Unknown Knowns
    quadrant-2 Known Unknowns
    quadrant-3 Unknown Unknowns
    quadrant-4 Known Unknowns
    e.g Behavior-based analysis: [0.7, 0.2]
```

All of this is based on the concept of a [Johari Window.](https://www.mindtools.com/au7v71d/the-johari-window)