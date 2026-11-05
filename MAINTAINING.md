# 维护与交接

本手册以 GitHub 仓库中的 Markdown 为内容来源，`main` 是发布分支。贡献者从 Fork 提交 PR，维护者审核并合并；GitBook Git Sync 将 `main` 同步到公开站点。站点级映射由 `gitbook-docs.yaml` 管理，`SUMMARY.md` 决定手册导航。

- 仓库：[hitwh-survival-compass](https://github.com/zuquanzhi/hitwh-survival-compass)
- 站点：[哈威求生指北](https://hitwh-survival-compass.gitbook.io/hitwh-survival-compass-docs/)
- 审核与写作要求：[贡献指南](CONTRIBUTING.md)

Git Sync 是双向的。为遵守 PR 流程，内容、目录和站点映射应通过 GitHub PR 修改，不在 GitBook 编辑器直接更改已同步内容或合并变更。GitBook 的外观、站点公开状态和同步配置在平台管理，设置变更应由维护者记录。

## 审核与发布

1. 在 PR 中确认修改目的、适用范围、来源和时间。政策或数据应能追溯到原始来源；个人经验需标明背景，并尊重不同观点。
2. 检查隐私、素材授权、相对链接、图片替代文字和 `SUMMARY.md`。不要把待核实内容当作事实，也不要要求贡献者公开不必要的个人信息。
3. 查看自动检查结果，人工阅读页面；如 GitBook 提供 PR 预览，可核对桌面和移动端导航、首页与文章样式。检查通过不等于事实已核实。
4. 请维护者完成 Review 并在 GitHub 合并，推荐使用 Squash Merge。记录必要的后续维护事项；不要在未审核的情况下绕开分支保护。
5. 检查 GitBook 同步状态和公开站点，确认合并的内容、链接和导航更新。发生异常时，先记录 GitHub 提交、GitBook 同步状态和页面现象，再排查。

## 本地与自动检查

在仓库根目录运行 `python scripts/check.py`（Windows 也可使用 `py -3 scripts/check.py`）。它只检查基础文件和简单相对 Markdown 链接；不验证锚点、外链可用性、图片呈现、事实、完整 Markdown 或实际同步。PR 和 `main` 的 GitHub Actions 运行相同检查；遇失败先阅读日志，修复后在同一 PR 追加提交。

## GitHub 配置

由仓库管理员核实 Settings → General 中已启用 Squash Merge；在 Settings → Rules → Rulesets 或 Branches 配置 `main` 保护：要求 PR、审核及必要的状态检查，并检查管理员、GitBook App 和其他角色是否有绕过权限。界面选项和适用限制以账号当前状态为准。

Git Sync 具有双向写入能力。启用保护后，以测试 PR 验证 GitHub → GitBook 同步与 GitBook App 权限；若规则产生冲突，先确认原因与影响，避免为方便直接允许未经审核的内容进入 `main`。

## GitBook 首次连接与恢复

仅在需要重新连接时操作：确认仓库和目标 `main` 分支正确、`gitbook-docs.yaml` 存在；GitBook 站点的 Git Sync 选择该仓库和分支，首次导入方向选择 **GitHub → GitBook**。确认现有 GitBook 内容不会被意外覆盖。同步完成后检查导航与公开地址。GitBook GitHub App 尽量只授予本项目仓库必要权限。

同步失败时，依次核对 PR 是否已合并、GitBook 连接的仓库与分支、同步日志、GitHub App 权限、分支保护和站点发布状态。不要在排障时从 GitBook 反向覆盖 GitHub 现有内容。

## 回滚与交接

发现错误时先评估是否需要暂时撤下相关内容；在 GitHub 找到相关合并提交，使用 revert 创建撤销提交，并通过 PR 审核合并。若撤回会影响后续提交，先人工解决冲突并验证。合并后核对 GitBook 与公开页面；Git 历史不会因为回滚而消失。

交接时至少确认：

- GitHub 仓库管理员和维护者、GitBook 组织及站点管理员的身份和联系方式；在可用方案允许的情况下安排可靠的备用管理方式，不共享个人密码。
- PR、审核、分支保护、GitHub App 授权与 Git Sync 状态；实际测试一条从 PR 到发布的流程。
- 站点地址、外观配置、图标源文件、已知问题、未处理 PR 和过期内容。
- 内容许可证和社区私下联系渠道。许可证尚未确定，维护者应在正式接收外部贡献前公布授权条款。
- 当前套餐、试用到期时间及费用。若仍处于 Ultimate 试用期，应在到期前核实免费方案如何切换以及站点是否仍可公开访问；不要擅自启用付费功能。

## 迁移和访问

保留 Markdown、资源、`SUMMARY.md` 和完整 Git 历史，并定期验证备份可读取。迁移时先在新环境验证导航、链接、搜索和移动端，再通知读者；旧地址的跳转能力取决于平台与方案。校内网及移动网络的访问速度、图片和搜索功能应分别实测，不能仅凭管理后台预览判断。

参考：[GitBook Git Sync 导入](https://gitbook.com/docs/guides/editing-and-publishing-documentation/import-or-migrate-your-content-to-gitbook-with-git-sync) · [GitBook 价格](https://www.gitbook.com/pricing) · [GitHub Pages 限制](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)
