"""How-to guides for the blog. Each one answers a search people already make and ends with the matching app.
Set "live": True to publish a guide; build.py skips drafts unless PREVIEW_DRAFTS=1."""

GUIDES = [
    {
        "slug": "recurring-issues-jira-cloud",
        "app": "recurring-issues",
        "live": False,
        "title": "How to create recurring issues in Jira Cloud",
        "date": "December 2026", "iso": "2026-12-01", "minutes": 5,
        "desc": "Three ways to create repeating Jira issues on a schedule (daily standups, weekly reports, monthly reviews), and when each one fits.",
        "body": """
<p class="lead">Jira Cloud has no "repeat this issue" button. If your team has a weekly report, a monthly access review or a daily standup ticket, someone has to remember to create it, or you set it up once with one of the three options below.</p>

<h2>Option 1: Jira Automation with a scheduled trigger</h2>
<p>Jira's built-in automation can create an issue on a schedule.</p>
<ol>
  <li>Go to <strong>Project settings → Automation</strong> and choose <strong>Create rule</strong>.</li>
  <li>Pick the <strong>Scheduled</strong> trigger and set the interval, for example every Monday at 09:00. For anything more specific, use a cron expression.</li>
  <li>Add the action <strong>Create issue</strong> and fill in the summary, issue type and assignee. Smart values such as <code>{{now.format("yyyy-MM-dd")}}</code> add the date to the title.</li>
  <li>Turn the rule on.</li>
</ol>
<p><strong>Good for:</strong> one or two simple schedules in a single project.</p>
<p><strong>Watch out for:</strong></p>
<ul>
  <li>Every run counts toward your plan's monthly automation limit.</li>
  <li>Schedules beyond "every N days" need cron syntax.</li>
  <li>The new issue is not added to the active sprint unless you add more steps.</li>
  <li>With many rules it is hard to see which schedule creates what.</li>
</ul>

<h2>Option 2: Clone a template issue</h2>
<p>Keep one "template" issue per routine task and clone it when needed: manually, or with an automation rule that clones it on a schedule. Cloning copies the description, labels and sub-tasks.</p>
<p><strong>Good for:</strong> routine work with a long checklist of sub-tasks.</p>
<p><strong>Watch out for:</strong> template issues show up in searches and boards unless you hide them, and you still need a schedule (option 1) or a person to do the cloning.</p>

<h2>Option 3: A recurring-issues app</h2>
<p>A dedicated app keeps every schedule in one list and handles the details the other options leave to you.</p>
<p><a href="/recurring-issues/">Recurring Issues for Jira</a> is ours:</p>
<ul>
  <li><strong>Plain-language schedules:</strong> every weekday, every second Monday, the last day of the month. A preview shows the next five runs, so no cron is needed.</li>
  <li><strong>Time zone per rule:</strong> 09:00 stays 09:00 after daylight saving changes.</li>
  <li><strong>Sprint-aware:</strong> new issues can go straight into the active sprint, and the previous unfinished copy can be closed automatically.</li>
  <li><strong>Placeholders</strong> such as <code>{{date}}</code>, <code>{{weekday}}</code> and <code>{{week}}</code> in titles and descriptions.</li>
</ul>
<p>It runs entirely on Atlassian and does not use your automation limit.</p>

<h2>Which one should you use?</h2>
<ul>
  <li><strong>One simple weekly issue:</strong> Jira Automation is enough.</li>
  <li><strong>A long checklist that repeats:</strong> clone a template issue, or use <a href="/issue-templates/">Issue Templates</a>.</li>
  <li><strong>Many schedules, several teams or time zones, sprint-based work:</strong> a recurring-issues app saves time and avoids missed tickets.</li>
</ul>
""",
    },
    {
        "slug": "confluence-page-approval-workflow",
        "app": "page-approval",
        "live": True,
        "title": "Confluence page approval: how to set up a review and sign-off workflow",
        "date": "November 2026", "iso": "2026-11-26", "minutes": 5,
        "desc": "How to get Confluence pages reviewed and approved, keep an audit trail for ISO or SOC 2, and know when an approved page has changed.",
        "body": """
<p class="lead">Policies, procedures and release notes often need a named person to approve them before they count. In audits (ISO 27001, SOC 2, GxP) you also need to show <em>who</em> approved <em>which version</em>, and that nobody changed the page afterwards. Here is what Confluence Cloud gives you, and where it stops.</p>

<h2>What Confluence offers on its own</h2>
<ul>
  <li><strong>Page status</strong> (for example "In progress", "Ready for review", "Verified"). This is a label anyone with edit rights can set. It does not record an approver and does not reset when the page changes.</li>
  <li><strong>Restrictions:</strong> you can limit who may edit a page, which keeps drafts safe but is not an approval.</li>
  <li><strong>Comments and @mentions:</strong> reviewers can say "approved" in a comment. That works for small teams, but there is no overview and no link to the version that was approved.</li>
  <li><strong>Page history:</strong> shows every version, but you have to match versions to approvals yourself.</li>
  <li><strong>Native Approvals (beta, Premium and Enterprise only):</strong> Atlassian is rolling out built-in page approvals on the higher plans. They require <em>every</em> approver to sign off (there is no "any one of them" option), and they are not available on Free or Standard. If you are on Premium, try them first.</li>
</ul>

<h2>What an approval workflow needs</h2>
<ol>
  <li><strong>Named approvers</strong>, with a rule: everyone must approve, or any one of them.</li>
  <li><strong>A visible status</strong> on the page: pending, approved, changes requested.</li>
  <li><strong>Approval tied to a version:</strong> if the page changes after approval, the approval is no longer valid.</li>
  <li><strong>An audit trail:</strong> who decided, when, on which version, with their comment.</li>
  <li><strong>An overview:</strong> what is waiting for me, and what is outdated.</li>
</ol>

<h2>Setting it up with Page Approval for Confluence</h2>
<p><a href="/page-approval/">Page Approval for Confluence</a> adds exactly these pieces on any Confluence plan, including Standard:</p>
<ol>
  <li>Open a page and choose <strong>Request approval</strong> next to the author name.</li>
  <li>Pick the approvers, choose <em>all</em> or <em>any</em>, and optionally set a due date. Approvers are notified through normal Confluence @mentions.</li>
  <li>Approvers <strong>approve</strong> or <strong>request changes</strong> right on the page, with a comment.</li>
  <li>The status shows next to the author: <em>Approval pending 1/2</em>, <em>Approved v5</em> or <em>Changes requested</em>.</li>
  <li>When someone publishes v6, the page shows <strong>Approval outdated</strong>. If the page changes during a review, earlier decisions are reset, so nobody approves text they haven't seen.</li>
  <li>Each space gets an <strong>Approvals</strong> page with a "Waiting for me" list and every request with its full history.</li>
</ol>
<p>Status labels also work in Confluence search and CQL, so you can build a report of every approved, or outdated, policy page.</p>

<h2>Tips for audits</h2>
<ul>
  <li>Use default approvers per space (for example the policy owner) so nobody forgets to add them.</li>
  <li>Before an audit, search for <em>Approval outdated</em> to find pages that changed since sign-off.</li>
  <li>Use the space's Approvals page as evidence of review: every decision is listed with its page version.</li>
</ul>
""",
    },
    {
        "slug": "confluence-questions-and-answers",
        "app": "qa-for-confluence",
        "live": True,
        "title": "Internal Q&A in Confluence: questions and answers your team can actually find",
        "date": "November 2026", "iso": "2026-11-26", "minutes": 4,
        "desc": "How to run an internal Q&A or FAQ inside Confluence, so answers stop disappearing in chat and people can search for them later.",
        "body": """
<p class="lead">The same questions get asked in chat every week: "Where is the VPN guide?", "Who approves travel?", "How do I get a test account?". The answers scroll away, and the next person asks again. An internal Q&amp;A in Confluence keeps those answers where people already search.</p>

<h2>Option 1: An FAQ page</h2>
<p>A single page with headings for each question is quick to start. It works while the list is short and one person maintains it.</p>
<p>It stops working when:</p>
<ul>
  <li>many people need to ask, so questions go back to chat;</li>
  <li>the page grows past a few dozen answers;</li>
  <li>nobody knows which answers are outdated.</li>
</ul>

<h2>Option 2: Questions as pages with a page template</h2>
<p>Create a "Question" page template and ask people to create one page per question, with answers as comments. Everything is searchable, but there is no accepted answer, no voting, and no list of unanswered questions. Someone has to watch for new pages.</p>

<h2>Option 3: A Q&amp;A app built on Confluence pages</h2>
<p>Some Q&amp;A apps keep questions in their own storage, which Confluence search cannot see. <a href="/qa-for-confluence/">Q&amp;A for Confluence</a> stores every question as a real Confluence page and every answer as a comment, so:</p>
<ul>
  <li>Confluence search finds words <strong>inside answers</strong>, not just question titles;</li>
  <li>space permissions decide who can see and answer;</li>
  <li>watchers get normal Confluence notifications;</li>
  <li>your questions stay in Confluence even if you uninstall the app.</li>
</ul>
<p>On top of that you get:</p>
<ul>
  <li>accepted answers, chosen by the asker or a space moderator;</li>
  <li>voting and tags;</li>
  <li>an <strong>Unanswered</strong> queue for experts;</li>
  <li>a FAQ of solved questions in the order your moderators choose;</li>
  <li>a macro that embeds questions with an Ask button on any page.</li>
</ul>

<h2>Getting people to use it</h2>
<ul>
  <li>Seed it with the ten questions you hear most often, before you announce it.</li>
  <li>When a question comes up in chat, answer with a link to the Q&amp;A instead of the answer itself.</li>
  <li>Give each space one or two moderators who check the Unanswered queue weekly.</li>
</ul>
""",
    },
    {
        "slug": "jira-cascading-select-more-levels",
        "app": "cascading-select",
        "live": True,
        "title": "Jira cascading select with more than two levels",
        "date": "November 2026", "iso": "2026-11-26", "minutes": 4,
        "desc": "Jira's built-in cascading select stops at two levels. How to get three to six dependent dropdowns, such as Region › Country › City.",
        "body": """
<p class="lead">Jira's built-in <strong>Select List (cascading)</strong> field has exactly two levels: a parent and a child. That covers Country › City, but not Region › Country › City, or Product › Component › Area. Here are your options.</p>

<h2>Option 1: Two-level cascading select plus a second field</h2>
<p>Use the built-in cascading field for the first two levels and a separate select list for the third. It is free, but the third list cannot depend on the first two: people see every option, and invalid combinations get through.</p>

<h2>Option 2: Combine levels into one option</h2>
<p>Put two levels into one option, such as "Europe – Germany" › "Berlin". It works for small trees, but the option list grows fast and reports become harder to read.</p>

<h2>Option 3: A multi-level cascading select field</h2>
<p><a href="/cascading-select/">Cascading Select for Jira</a> adds a field type with <strong>up to six dependent levels</strong>. Each dropdown only offers the options under the one chosen above it.</p>
<ol>
  <li>In <strong>Jira settings → Issues → Custom fields</strong>, create a field of type <em>Multi-level select (Loopwise)</em> and add it to your screens.</li>
  <li>In the field's configuration, <strong>type or paste the whole option tree as an indented list</strong>. Indent to nest.</li>
</ol>
<pre><code>Europe
  Germany
    Berlin
    Munich
  France
    Paris
North America
  USA
    New York</code></pre>
<ol start="3">
  <li>Optionally name the levels (Region, Country, City) and require a choice down to the last level.</li>
</ol>
<p>The value is stored as plain text, such as <code>Europe › Germany › Berlin</code>, so it shows up cleanly in exports, filters and dashboards and can be searched by exact value. It works on create, edit and transition screens in company-managed projects.</p>

<h2>Which one should you use?</h2>
<ul>
  <li><strong>Two levels are enough:</strong> use the built-in field.</li>
  <li><strong>Three or more levels, and wrong combinations matter</strong> (routing, reporting, SLAs): use a multi-level field.</li>
</ul>
""",
    },
    {
        "slug": "export-jira-issues-to-pdf-word",
        "app": "issue-export",
        "live": True,
        "title": "How to export Jira issues to PDF or Word (one issue or a whole list)",
        "date": "November 2026", "iso": "2026-11-27", "minutes": 5,
        "desc": "Ways to export a Jira Cloud issue, or the result of a JQL search, to PDF or Word: built-in options, their limits, and when an export app is worth it.",
        "body": """
<p class="lead">A customer wants a report of the open bugs, an auditor wants the change request with every comment, or a manager wants the sprint scope as a Word document. Jira Cloud has a few built-in ways to get issues out, and each has limits worth knowing before you promise a document.</p>

<h2>Option 1: Print one issue to PDF</h2>
<p>Open the issue, choose <strong>••• → Print</strong>, and in the print dialog pick <strong>Save as PDF</strong>.</p>
<p><strong>Good for:</strong> a quick copy of a single issue.</p>
<p><strong>Watch out for:</strong> the layout follows the browser, long descriptions and tables often break across pages, and you get one issue at a time.</p>

<h2>Option 2: The built-in Word export</h2>
<p>On an issue, <strong>••• → Export Word</strong> downloads a .doc file with the issue's fields and description.</p>
<p><strong>Watch out for:</strong> it is an older HTML-based format, so Word may warn when opening it, formatting of tables and code blocks is basic, and sub-tasks and comments are limited.</p>

<h2>Option 3: Export a search to CSV or Excel</h2>
<p>Run a JQL search in <strong>Filters</strong>, then use <strong>Export</strong> to download CSV with all or the current fields. Open it in Excel or Google Sheets and format it there.</p>
<p><strong>Good for:</strong> data you want to analyse.</p>
<p><strong>Watch out for:</strong> it is a spreadsheet, not a document. Rich text (headings, lists, tables in the description) arrives as markup, and you have to build the report yourself every time.</p>

<h2>Option 4: An export app</h2>
<p>An export app turns issues into documents in one click. <a href="/issue-export/">Issue Export for Jira (PDF &amp; Word)</a> is ours:</p>
<ul>
  <li><strong>One issue, complete:</strong> details, the full rich-text description (headings, lists, tables, code, panels), sub-tasks and comments.</li>
  <li><strong>Any JQL as a table:</strong> choose the columns, up to 1,000 issues, landscape when there are many columns; or one page per issue.</li>
  <li><strong>PDF or real .docx</strong> that opens cleanly in Word.</li>
  <li><strong>Download or attach</strong> the file to the issue as a record.</li>
  <li>Documents are made in your browser with your Jira permissions, and the app stores nothing.</li>
</ul>

<h2>Which one should you use?</h2>
<ul>
  <li><strong>One issue, once in a while:</strong> Print to PDF is enough.</li>
  <li><strong>Data for analysis:</strong> CSV export.</li>
  <li><strong>Documents you send to customers, auditors or managers, regularly:</strong> an export app saves the formatting work every time.</li>
</ul>
""",
    },
    {
        "slug": "jira-project-cost-tracking-without-tempo",
        "app": "cost-tracker",
        "live": True,
        "title": "How to track project costs and budgets in Jira (without Tempo)",
        "date": "November 2026", "iso": "2026-11-27", "minutes": 6,
        "desc": "Jira tracks hours, not money. Here is how to turn Jira worklogs into project costs and budgets: with a spreadsheet, with Tempo, or with a lightweight cost app.",
        "body": """
<p class="lead">Jira knows how many hours your team logged, but not what those hours cost. When someone asks "how much has this project cost so far, and will we stay within budget?", you need hourly rates, a budget and a forecast on top of Jira's time tracking.</p>

<h2>What Jira gives you out of the box</h2>
<ul>
  <li><strong>Worklogs:</strong> time logged on each issue, by person and date.</li>
  <li><strong>Original and remaining estimates:</strong> how much work is planned and left.</li>
  <li><strong>Time tracking reports</strong> in some project types, in hours only.</li>
</ul>
<p>There are no rates, no money and no budgets.</p>

<h2>Option 1: Export worklogs to a spreadsheet</h2>
<p>Export the issues and their time spent with a JQL search (CSV), add a rate per person in a second sheet, and multiply.</p>
<p><strong>Good for:</strong> a one-off answer.</p>
<p><strong>Watch out for:</strong> it is manual every time, the issue export gives total time per issue rather than who logged what and when, and rates that change over time make the formulas fragile. The numbers are out of date the moment you save the file.</p>

<h2>Option 2: Tempo</h2>
<p>Tempo Timesheets with a financial add-on is the classic answer for larger organisations. It is powerful, but it means moving your team to Tempo's timesheets, and paying for several products per user.</p>

<h2>Option 3: A cost app on top of Jira's own worklogs</h2>
<p>If your team already logs time in Jira, a lightweight cost app can read those worklogs directly. <a href="/cost-tracker/">Cost &amp; Budget Tracker for Jira</a> is ours:</p>
<ul>
  <li><strong>Hourly rates per person</strong>, each with the date it starts, so past work keeps its old price after a raise.</li>
  <li><strong>Budgets</strong> for a project, several projects or any JQL, with an optional period.</li>
  <li><strong>Spent, forecast and remaining:</strong> the forecast adds remaining estimates at each assignee's rate, with On track or Over budget status.</li>
  <li><strong>A Costs page in every project:</strong> cost per person, per month and per epic.</li>
  <li><strong>Private by default:</strong> only Jira admins and the people they choose see rates and amounts.</li>
</ul>
<p>No Tempo and no new timesheets: it uses the worklogs you already have.</p>

<h2>Tips for reliable numbers</h2>
<ul>
  <li>Ask everyone to log time on the issue they worked on, not on one "general" ticket.</li>
  <li>Keep remaining estimates current, or the forecast is only as good as the last update.</li>
  <li>Set rates with start dates instead of editing old rates, so historic costs don't change.</li>
</ul>
""",
    },
    {
        "slug": "questions-for-confluence-alternative",
        "app": "qa-for-confluence",
        "live": True,
        "title": "Looking for a Questions for Confluence alternative?",
        "date": "November 2026", "iso": "2026-11-27", "minutes": 4,
        "desc": "What to look for in a Q&A app for Confluence Cloud, and how to move your team's questions and answers to an app built on regular Confluence pages.",
        "body": """
<p class="lead">If your team relies on Questions for Confluence and recent problems (questions that don't show up, search that misses answers) have you looking for an alternative, here is what to check before you switch, and how Q&amp;A for Confluence handles it.</p>

<h2>What to look for in a Confluence Q&amp;A app</h2>
<ul>
  <li><strong>Where questions are stored.</strong> If the app keeps them in its own storage, Confluence search can't find them and they disappear when you uninstall. Content stored as Confluence pages and comments stays yours.</li>
  <li><strong>Search inside answers.</strong> People search for the problem, which is usually in the answer, not the question title.</li>
  <li><strong>Permissions.</strong> Questions should follow space permissions, with no separate access model to manage.</li>
  <li><strong>Accepted answers and an Unanswered queue,</strong> so experts know what still needs help.</li>
  <li><strong>Runs on Atlassian,</strong> so your data never leaves your Atlassian site.</li>
</ul>

<h2>How Q&amp;A for Confluence works</h2>
<p><a href="/qa-for-confluence/">Q&amp;A for Confluence</a> stores every question as a Confluence page and every answer as a comment:</p>
<ul>
  <li>Confluence search finds words inside answers;</li>
  <li>space permissions and watchers work as usual;</li>
  <li>accepted answers, voting, tags and an Unanswered queue;</li>
  <li>a FAQ of solved questions, ordered by moderators;</li>
  <li>a macro with an Ask button for any page;</li>
  <li>free for up to 10 users, and it runs entirely on Atlassian.</li>
</ul>

<h2>Moving your questions</h2>
<ol>
  <li>Install Q&amp;A for Confluence and open <strong>Questions</strong> in the space.</li>
  <li>Start with your most-viewed questions: ask each one again and paste the accepted answer, so the FAQ is useful on day one.</li>
  <li>Link old question pages to their new place, or archive them once the team uses the new Q&amp;A.</li>
  <li>Announce it with a short note: "Ask here instead of chat, answers stay searchable."</li>
</ol>
<p>Need help moving a large number of questions? <a href="/support/">Contact us</a>.</p>
""",
    },
    {
        "slug": "jira-gantt-chart-multiple-projects",
        "app": "gantt",
        "live": True,
        "title": "Gantt chart for multiple Jira projects: your options in Jira Cloud",
        "date": "November 2026", "iso": "2026-11-27", "minutes": 5,
        "desc": "How to see issues from several Jira Cloud projects on one Gantt chart with dependencies: Timeline, Plans (Premium) and Gantt apps compared.",
        "body": """
<p class="lead">One project on a timeline is easy in Jira. Several projects, with dependencies between them and dates you can drag, is where teams start looking for a Gantt chart. Here is what Jira Cloud offers and when an app makes sense.</p>

<h2>Option 1: The project Timeline</h2>
<p>Every software project has a <strong>Timeline</strong> view with epics and child issues as bars.</p>
<p><strong>Good for:</strong> one team, one project, epic-level planning.</p>
<p><strong>Watch out for:</strong> it shows one project at a time, and the detail below epics is limited.</p>

<h2>Option 2: Plans (Jira Premium)</h2>
<p><strong>Plans</strong> (formerly Advanced Roadmaps) combines several projects and boards, with dependencies and capacity.</p>
<p><strong>Good for:</strong> organisations already on Premium that need portfolio planning.</p>
<p><strong>Watch out for:</strong> it requires the Premium plan for everyone on the site, and it takes setup and training.</p>

<h2>Option 3: A Gantt app</h2>
<p>A Gantt app gives you a classic chart across projects on any Jira plan. <a href="/gantt/">Gantt Chart for Jira</a> is ours:</p>
<ul>
  <li><strong>Several projects or any JQL</strong> in one saved plan, private or shared.</li>
  <li><strong>Hierarchy:</strong> epics, stories and sub-tasks with expand and collapse.</li>
  <li><strong>Drag to reschedule:</strong> new dates are saved to Jira at once, with your permissions, and Ctrl+Z undoes it.</li>
  <li><strong>Dependencies:</strong> "blocks" links drawn as arrows; a successor that starts too early turns red.</li>
  <li><strong>Milestones:</strong> release dates, a today line, and zoom by day, week, month or quarter.</li>
  <li><strong>Safe by design:</strong> it only changes the start and due dates of issues you drag, and never deletes anything.</li>
</ul>

<h2>Which one should you use?</h2>
<ul>
  <li><strong>One project, epics only:</strong> the built-in Timeline.</li>
  <li><strong>Portfolio planning on Premium:</strong> Plans.</li>
  <li><strong>Several projects on Standard, or issue-level Gantt with dependencies:</strong> a Gantt app.</li>
</ul>
""",
    },
]
