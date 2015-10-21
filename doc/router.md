# router

** 约定路由，方便后续使用。**
** 大体上采用前台拉取后台数据，后台采用类`restful`风格接口,统一 `json`传值 **

## 载入首页

+ url: /
+ method: get

## 注册
+ url: /reg
+ method: post
+ response:
  * -1  用户名已经被注册
  * -2  邮箱已经被注册
  * -3  其他（满足前端验证但不满足后端验证）
  * 1   登录成功

## 登录
+ url: /login
+ method: /post
+ reponse:
  * 0  密码错误
  * 1  成功登录




















*********************************

## 展示URL

### 首页
```
/                                             ---  Get
```

### 用户
```
/u/:id/                                      ---  Get                    ---  User
```

### 活动
```
/activity/
/activity/:id/
```

### 景点
```
/scenery/
/scenery/:id/
```


## AJAX 请求URL

### 首页
```
/login/                                      ---  Post                   ---  User
/reg/                                        ---  Post                   ---  User
/activity/:number/                           ---  Get                    ---  Activity/ActivityUser/Scenery/ActivityScenery
/scenery/:number/
/journal/:number/
```

### 用户中心
```
/u/:id/update/
/u/:id/changepassword/
/u/:id/comment
```

### 活动
```
/activity/add/
/activity/scenery?name=/
```

### 景点
```
/scenery/:id/comment
```

