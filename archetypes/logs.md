---
title: "{{ replace .Name "-" " " | title }}"
commander: ""
date: {{ .Date }}
location: ""
system: "HIP 22460"
type: log
series: ""
log_number: 0
weight: 0
tags:
  - thargoid
draft: false
prev_log: ""
next_log: ""
---

[{{ .Date.Format "2006-01-02 1504 UTC" }}]
RESEARCH LOG ENTRY
-----------------
Location: {{ .Params.location }}

[Log Entry Content]

Equipment Note: Analysis performed using ThargoidSignalAnalyzer toolkit v1.0.0 