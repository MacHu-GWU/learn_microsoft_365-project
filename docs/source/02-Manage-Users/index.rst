Manage Users
==============================================================================
这篇文档主要讲作为管理员如何管理 Office 下的 User. 在这一节中我们将会介绍如何:

- 如何创建用户
- 如何给予用户适当的权限
- 如何让一个指定另一个用户作为管理员来协助你管理其他的用户
- 以及如何通过 Team 和 Group 来批量管理用户


Sign In
------------------------------------------------------------------------------
首先要确保你是 `Global Admin <https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide>`_, 也就是这个 Microsoft 365 Plan 的 Owner, 你负责付款, 以及你对这个账号下的所有东西有最终所有权.

然后你就要用你的 email 和 password login. 本质上你也是一个 User, 只不过你有 Global Admin 的权限.

1. Go to https://www.office.com/, click "Sign in" button on the top right.

.. image:: ./office-login-1.png

2. Click the Admin button to enter the Admin Management page (https://admin.microsoft.com/Adminportal/Home#/homepage).

.. image:: ./office-login-2.png


Manage Users
------------------------------------------------------------------------------
要管理公司员工的 User Account, 例如为新雇员创建 User, 可以点击左侧的 Users -> Active Users 菜单. 在这一菜单下你可以看到公司所有的员工列表, 以及 Add User 的按钮. 你还可以选中一个 User 对它进行管理.

.. image:: ./manage-users-1.png

当公司有雇员时, 可以用 Add User 按钮来创建一个新用户. 创建的过程有三部:

1. 填名字等基本信息.
2. Product License, 决定了这个用户能用哪些产品.
3. Role, 决定了这个用户在 Microsoft 365 公司中的管理员权限. 这个权限定义了这个用户能在 Microsoft 365 中对进行哪些管理类型的操作, 这个权限跟能不能访问 OneDrive, Word, Excel, PPT 没有关系. 下面一节我们会详细讲这个 Role 的概念.


Manage Roles
------------------------------------------------------------------------------
由于老板的精力是有限的, 一般需要让一个雇员而不是老板本人来协助管理 Office 365 中的 User. 这种需求可以由 Admin Roles 功能实现.

我们来看一个 User Detail Info 的例子. 我们选中 SA 这个 User, 可以看到他的详细信息. 里面有这个 User 的 Roles 信息.

.. image:: ./manage-users-2.png

点开之后就能看到这个用户的 Roles. 每个 Roles 的详细解释可以在 `Commonly used Microsoft 365 admin center roles <https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide#commonly-used-microsoft-365-admin-center-roles>`_ 文档中找到. 根据名字可以直观的看到 User Administrator 有管理 Users 的权限, Teams Administrator 有管理 Teams 和 Groups 的权限 (Teams 和 Groups 的概念我们之后会说).

.. image:: ./manage-users-3.png


Guest User
------------------------------------------------------------------------------
当需要与外部人员进行合作时 (如临时合作人员或服务供应商), 我们可以将他们作为 Guest User 邀请到组织中. Guest User 可以通过自己的邮箱访问特定的协作功能, 例如在 Microsoft Teams 中与内部员工进行沟通, 接收内部员工的邮件, 以及共享特定文件等. 需要注意的是, Guest User 的访问权限是受限的, 他们无法访问公司内部普通用户的 SharePoint 站点或共享的 OneDrive 文件夹. 通常的做法是, 在邀请 Guest User 加入组织后, 为其创建专门的 Microsoft Teams. 在这个特定的 Teams 空间内, Guest User 可以获得对应的 OneDrive 子文件夹访问权限, 并能与被添加到同一 Teams 中的内部成员进行协作. 这种方式既能确保外部人员与内部员工进行必要的协作, 又可以有效控制其访问权限. 

注:

- Guest User 不会产生任何费用.
- Guest User 不会自动获得任何 OneDrive 的访问权限. 他只能访问他所在的 Team 中的 Shared Folder (在 Microsoft Teams 中可以看到)

Reference:

- `about guest users <https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-guest-users?view=o365-worldwide>`_
