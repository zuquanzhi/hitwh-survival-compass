# 维护与发布

## 架构与方案

站点级同步配置位于 `gitbook-docs.yaml`，仓库根目录映射为一个手册空间，`SUMMARY.md` 管理页面导航。`assets/compass.svg` 是项目指南针标识源文件。

GitHub 保存 Markdown 和历史，贡献通过 Fork → PR → Review → 合并到 `main`；GitBook 的 Git Sync 将 `main` 的内容同步到公开站点。Git Sync 是双向的，维护者应只通过 GitHub PR 修改内容，不在 GitBook 编辑器直接修改或合并，以免绕过审核。站点外观和发布设置在 GitBook 管理。无本地构建步骤或运行时依赖。

交大生存手册采用 Markdown、README 和 SUMMARY，并使用 GitBook；CS First Aid 则使用 pnpm workspace 等较复杂的项目结构。本项目只借鉴文档组织和阅读体验。GitBook 免费方案包含公开站点、全文搜索与 Git Sync，只有一个用户席位；GitHub PR 贡献者不需要 GitBook 席位。免费版不包括站点 PDF 导出和自定义域名，具体以开通时的价格页为准。GitBook 是托管服务，其可用性、价格和功能可能变化；通用 Markdown 与 Git 历史便于迁移。作为备选，Starlight 是静态站点方案，公开仓库可使用 GitHub Pages 和标准 GitHub Actions 免费额度，但需要维护构建和配置；当前不搭建第二套站点。

大陆校园网访问 GitHub、GitBook 及其静态资源的速度和稳定性可能因网络及时间而异，尚未进行校园网实测。发布后请在校内网、移动网络分别测试主页、搜索、图片和 GitHub 入口，再决定是否需要其他合规托管方式。

## 首次发布：由仓库及 GitBook 管理员操作

1. 确定内容许可证和社区联系方式。GitHub 仓库已配置为 `zuquanzhi/hitwh-survival-compass`；由授权人员推送本地 `main`，并确认仓库为公开状态。
2. 在 GitHub 仓库 Settings → General 启用 squash merging。Settings → Rules → Rulesets（或 Branches）为 `main` 要求 PR 和至少一名审阅者，并按需要要求检查通过、限制绕过；确保维护者实际无法直接推送，注意管理员和 GitBook 应用的绕过权限。先确认保护规则与 Git Sync 的双向写入兼容，遇冲突时不要放宽 PR 审核而未评估。
3. 在 GitBook 创建组织和公开 Docs site，选择免费方案。站点级 Git Sync 需要仓库根目录中的 `gitbook-docs.yaml`；该文件已配置单一手册空间。安装 GitHub Sync 应用时优先只授权该仓库；在站点选择 Set up Git Sync，选择仓库和 `main`，首次同步方向选 **GitHub → GitBook**，避免空 Space 覆盖已有文件。
4. 同步完成后，将站点发布到平台提供的免费地址。当前地址为 https://hitwh-survival-compass.gitbook.io/hitwh-survival-compass-docs/ 。在站点设置中填写中文标题、描述和语言，添加真实 GitHub 仓库链接，并检查编辑入口、搜索、移动端和主题选项。免费计划的界面选项以实际账户为准。
5. 发起测试 PR，确认检查和审核流程；合并后确认 Git Sync 状态、站点页面和导航均更新。若未更新，检查 GitBook 同步日志、GitHub App 权限、分支保护及发布状态。

GitBook 管理员账号需要妥善交接；不要共享个人密码。GitHub 仓库应由多位可信维护者管理，未来可迁入独立 Organization。PR 合并后可用 Git 历史定位和回滚错误，再通过 PR 修复。

## 本地检查

安装 Python 3 后在仓库根目录运行 `python scripts/check.py`。检查导航目标、相对 Markdown 链接与基本结构；它不是完整的 Markdown 渲染器，也不能替代 GitBook 实际同步和页面预览。CI 在 PR 和推送 main 时运行同一检查。

## 参考资料

- [交大生存手册仓库](https://github.com/SurviveSJTU/SurviveSJTUManual)
- [CS First Aid 仓库](https://github.com/AndyBRoswell/cs-first-aid)
- [GitBook Git Sync 导入](https://gitbook.com/docs/guides/editing-and-publishing-documentation/import-or-migrate-your-content-to-gitbook-with-git-sync)
- [GitBook 价格](https://www.gitbook.com/pricing)
- [GitBook 开源项目方案](https://www.gitbook.com/solutions/open-source)
- [GitHub Pages 限制](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)
- [GitHub Actions 计费](https://docs.github.com/en/billing/concepts/product-billing/github-actions)

## 试用期和费用

当前站点创建时处于 Ultimate 试用期。维护者应在试用结束前核实降级为免费方案的具体步骤及站点功能，不要启用需付费的功能或假定试用结束后站点会自动维持公开。若显示费用或要求支付，请先确认再操作。
