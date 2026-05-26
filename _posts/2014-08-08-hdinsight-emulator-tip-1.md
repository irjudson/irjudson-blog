---
title: "HDInsight Emulator Tip #1"
date: 2014-08-08 18:38:25 +0000
categories: [technology]
tags: ["hadoop", "hdinsight", "technology"]
---

When developing map-reduce programs for Microsoft Azures Hadoop implementation, HDInsight, it's often useful to reference data stored in azure.

Here is what I've found works easily but wasn't clear from the examples discovered online:

- Add a configuration to your core-site.xml file:

`    
     fs.azure.account.key..blob.core.windows.net    
     STORAGE KEY
`

- Refer to the file you want to use as:

```
`wasb://@.blob.core.windows.net/`
```

---

*This post was migrated from WordPress. Original publication date: 2014-08-08 18:38:25*
