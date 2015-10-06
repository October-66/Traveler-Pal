# Class

** 修改model的时候一定要事先修改本文档，防止产生不必要的问题**

### User( 用户 )
```
id             ---      int      ---      primary auto     ---  唯一ID
username       ---      string                             ---  用户名
email          ---      email                              ---  邮箱
gender            ---      string                             ---  性别
password       ---      string   ---      md5              ---  密码（md5加密）
interest       ---      string                             ---  爱好兴趣
```

### Activity( 活动 )
```
id             ---      int      ---      primary auto     ---  唯一ID
name           ---      string                             ---  活动名称
```

### ActivityUser( 参加活动的人/一个活动可以是多个人参加 )
```
id             ---      int      ---      primary auto     ---  唯一ID
activityid     ---      int      ---      primary          ---  活动ID
userid         ---      int                                ---  参与活动的人员ID
```

### Scenery(景点)
```
id             ---      int      ---      primary auto     ---  唯一ID
name           ---      sring                              ---  景点名称
```

### ActivityScenery(活动要去的景点)
```
id             ---      int      ---      primary auto     ---  唯一ID
activityid     ---      int      ---      primary          ---  活动ID
sceneryid      ---      int      ---                       ---  景点ID
```

### Comment(评价)
```
id             ---      int      ---      primary auto     ---  唯一ID
content        ---      string                             ---  评论内容
```

### SceneryComment(对景点的评价)
```
id             ---      int      ---      primary auto     ---  唯一ID
sceneryid      ---      int      ---                       ---  景点ID
commentid      ---      int      ---                       ---  评价ID
```

### UserComment(用户发表过的评论)
```
id             ---      int      ---      primary auto     ---  唯一ID
userid         ---      int                                ---  用户ID
commentid      ---      int                                ---  评论ID
```

### Journal（日志）
```
id             ---      int      ---      primary auto     ---  唯一ID
title          ---      string                             ---  日志标题
content        ---      string                             ---  日志内容
```

### UserJournal（用户发表过的日志）
```
id             ---      int      ---      primary auto     ---  唯一ID
journalid      ---      int                                ---  日志ID
```
