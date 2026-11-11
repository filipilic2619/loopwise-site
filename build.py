"""Generates the static Loopwise Labs site. Edit the content below, run `python3 build.py`, commit."""
from pathlib import Path

DOMAIN = "loopwiselabs.app"
EMAIL = f"support@{DOMAIN}"
UPDATED = "10 November 2026"
ENTITY = ("Filip Ilić PR Agencija za računarsko programiranje Filip Code Kaona, "
          "registered in the Republic of Serbia, company ID (MB) 65422174, tax ID (PIB) 111454976, "
          "seat: Kaona, Serbia")
MARKETPLACE = "https://marketplace.atlassian.com/"  # replace with the app listing URL once approved

ROOT = Path(__file__).parent


def page(path, title, description, body):
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="/style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%233b5bdb'/%3E%3Ctext x='16' y='22' font-size='17' text-anchor='middle' fill='white' font-family='sans-serif' font-weight='700'%3EL%3C/text%3E%3C/svg%3E">
</head>
<body>
<header><div class="wrap">
  <a class="logo" href="/"><span>L</span>Loopwise Labs</a>
  <nav><a href="/recurring-issues/">Recurring Issues</a><a href="/qa-for-confluence/">Q&amp;A</a><a href="/page-approval/">Page Approval</a><a href="/epic-progress/">Epic Progress</a><a href="/issue-templates/">Issue Templates</a><a href="/support/">Support</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a></nav>
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer><div class="wrap">
  <p>© 2026 Loopwise Labs · <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="/dpa/">Data Processing Agreement</a></p>
  <p>{ENTITY}.</p>
</div></footer>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


page("index.html", "Loopwise Labs", "Small, reliable apps for Atlassian Cloud.", f"""
<h1>Small, reliable apps for Atlassian&nbsp;Cloud.</h1>
<p class="lead">Loopwise Labs builds focused apps that take repetitive work off your team's plate, running entirely on Atlassian's own infrastructure.</p>
<div class="card">
  <div class="pill">Jira Cloud · Runs on Atlassian</div>
  <h3>Recurring Issues for Jira</h3>
  <p>Create Jira issues on a schedule, in your time zone and your sprint, with no cron.</p>
  <a class="btn" href="/recurring-issues/">Learn more</a>
</div>
<div class="card">
  <div class="pill">Confluence Cloud · Runs on Atlassian</div>
  <h3>Q&amp;A for Confluence</h3>
  <p>Ask and answer questions inside Confluence, with search that finds answers, not just titles.</p>
  <a class="btn" href="/qa-for-confluence/">Learn more</a>
</div>
<div class="card">
  <div class="pill">Confluence Cloud · Runs on Atlassian</div>
  <h3>Page Approval for Confluence</h3>
  <p>Get pages approved by the right people, with approvals that expire when the page changes.</p>
  <a class="btn" href="/page-approval/">Learn more</a>
</div>
<div class="card">
  <div class="pill">Jira Cloud · Runs on Atlassian</div>
  <h3>Epic Progress for Jira</h3>
  <p>See how far every epic really is: issues, story points and time, rolled up with sub-tasks.</p>
  <a class="btn" href="/epic-progress/">Learn more</a>
</div>
<div class="card">
  <div class="pill">Jira Cloud · Runs on Atlassian</div>
  <h3>Issue Templates for Jira</h3>
  <p>Create issues with all their sub-tasks from a template, with variables like {{customer}} filled in.</p>
  <a class="btn" href="/issue-templates/">Learn more</a>
</div>
""")

page("issue-templates/index.html", "Issue Templates for Jira | Loopwise Labs",
     "Issue templates for Jira: create issues with sub-tasks or child issues from templates, with variables.", f"""
<div class="pill">Jira Cloud app</div>
<h1>Issue Templates for Jira</h1>
<p class="lead">Onboarding, releases, offboarding, audits: create the issue and every sub-task in one click, the same way every time.</p>
<ul class="features">
  <li><strong>Templates with sub-tasks:</strong> summary, description, issue type, priority, labels and a list of sub-tasks.</li>
  <li><strong>Variables:</strong> write <code>{{{{customer}}}}</code> or <code>{{{{contact}}}}</code> and people fill them in when they create the issue. <code>{{{{date}}}}</code>, <code>{{{{week}}}}</code>, <code>{{{{month}}}}</code> and <code>{{{{year}}}}</code> fill themselves in.</li>
  <li><strong>Add to an existing issue:</strong> "Add from template" in an issue's menu adds the template's sub-tasks, or child issues when it's an epic.</li>
  <li><strong>Per project or everywhere:</strong> make a template available in one project or in all of them.</li>
  <li><strong>Your permissions:</strong> issues are created as the person using the template, with their Jira permissions, and they are the reporter.</li>
  <li><strong>Admin control:</strong> optionally let only Jira admins create and edit templates.</li>
  <li><strong>No personal data stored:</strong> templates contain only the text you write.</li>
</ul>
<h2>Getting started</h2>
<ol>
  <li>Install the app from the Atlassian Marketplace.</li>
  <li>Open <em>Apps → Issue templates</em>, go to <em>Templates</em> and click <em>New template</em>.</li>
  <li>Use it under <em>Create issue</em>, or from <em>••• → Add from template</em> on any issue.</li>
</ol>
<h2>FAQ</h2>
<p><strong>A field from my template was not set.</strong> If priority or labels are not on the project's create screen, the issue is created without them instead of failing.</p>
<p><strong>What happens if my subscription ends?</strong> Templates are kept, but new issues can't be created from them until the license is active again.</p>
<p>Questions? <a href="/support/">Contact support</a>.</p>
""")

page("epic-progress/index.html", "Epic Progress for Jira | Loopwise Labs",
     "Epic progress for Jira: done, in progress and to do, story points and time tracking rolled up from child issues and sub-tasks.", f"""
<div class="pill">Jira Cloud app</div>
<h1>Epic Progress for Jira</h1>
<p class="lead">How far along is this epic, really? Issues, story points and time in one place, without building a dashboard.</p>
<ul class="features">
  <li><strong>On every epic:</strong> a Progress panel with done, in progress and to do, story points done, and time logged, remaining and estimated.</li>
  <li><strong>Sub-tasks included:</strong> time tracking uses Jira's aggregate fields, so work logged on sub-tasks counts.</li>
  <li><strong>What needs attention:</strong> overdue, unassigned and unestimated issues are flagged.</li>
  <li><strong>All epics of a project on one page:</strong> progress bars, points, time left and warnings, sorted by least progress or most work left.</li>
  <li><strong>Works for stories too:</strong> any issue with sub-tasks gets the same roll-up.</li>
  <li><strong>Stores nothing:</strong> the app only reads Jira, as the person viewing it, so everyone sees only what they already may see.</li>
</ul>
<h2>Getting started</h2>
<ol>
  <li>Install the app from the Atlassian Marketplace.</li>
  <li>Open an epic and expand <em>Progress</em> on the right.</li>
  <li>For a project overview, open the <em>Epic progress</em> tab in the project.</li>
</ol>
<h2>FAQ</h2>
<p><strong>Which story points field is used?</strong> The app finds "Story Points" and "Story point estimate" automatically, in company-managed and team-managed projects.</p>
<p><strong>How is time shown?</strong> In Jira's format with 8-hour days and 5-day weeks.</p>
<p><strong>What happens if my subscription ends?</strong> The panel and page show a notice until the license is active again. Nothing is stored, so there is nothing to clean up.</p>
<p>Questions? <a href="/support/">Contact support</a>.</p>
""")

page("page-approval/index.html", "Page Approval for Confluence | Loopwise Labs",
     "Page approvals for Confluence: approvers, all/any rules, due dates, audit trail, and approvals that expire when the page changes.", f"""
<div class="pill">Confluence Cloud app</div>
<h1>Page Approval for Confluence</h1>
<p class="lead">Know which version of a page was approved, by whom and when, and see at a glance when it changed afterwards.</p>
<ul class="features">
  <li><strong>Status next to the author:</strong> every page shows <em>Approval pending 1/2</em>, <em>Approved v5</em>, <em>Changes requested</em> or <em>Approval outdated</em> at the top.</li>
  <li><strong>Approvals that expire:</strong> when an approved page gets a new version it is marked <em>outdated</em>. If the page changes during review, earlier decisions are reset so nobody approves text they haven't seen.</li>
  <li><strong>Your rules:</strong> everyone must approve, or one approval is enough. Optional due dates with overdue markers.</li>
  <li><strong>Notifications without setup:</strong> approvers are @mentioned in a page comment, so Confluence notifies them as usual.</li>
  <li><strong>Audit trail:</strong> every request, decision and comment is kept with the page version it applied to.</li>
  <li><strong>Approvals page per space:</strong> Waiting for me, Pending, Approved, Changes requested and Outdated.</li>
  <li><strong>Space defaults:</strong> default approvers, default rule and approval managers who can cancel requests.</li>
  <li><strong>Native filtering:</strong> status labels such as <code>approval-approved</code> work in Confluence search, CQL and page lists.</li>
</ul>
<h2>Getting started</h2>
<ol>
  <li>Install the app from the Atlassian Marketplace.</li>
  <li>Open a page and click <em>Request approval</em> next to the page author.</li>
  <li>Pick approvers and a rule, optionally a due date and a note, and send.</li>
  <li>Optional: space admins can set default approvers and managers under <em>Space settings → Page Approval</em>.</li>
  <li>Optional: add the <em>Approval status</em> macro to a page body.</li>
</ol>
<h2>FAQ</h2>
<p><strong>Do approvers need edit permission?</strong> No. Anyone who can view the page and is named as approver can decide.</p>
<p><strong>What counts as a change?</strong> A new published version of the page. Comments, labels and the app's own updates do not count.</p>
<p><strong>What happens if my subscription ends?</strong> Statuses and history stay visible. New requests and decisions pause until the license is active again.</p>
<p>Questions? <a href="/support/">Contact support</a>.</p>
""")

page("qa-for-confluence/index.html", "Q&A for Confluence | Loopwise Labs",
     "Questions and answers inside Confluence, built on real pages: native search, permissions and notifications.", f"""
<div class="pill">Confluence Cloud app</div>
<h1>Q&amp;A for Confluence</h1>
<p class="lead">Your team's questions and answers, inside Confluence, where the knowledge already lives.</p>
<ul class="features">
  <li><strong>Search that finds answers:</strong> questions are real Confluence pages and answers are comments, so Confluence search covers both, not just titles.</li>
  <li><strong>Permissions you already have:</strong> each space's permissions decide who can see, ask and answer.</li>
  <li><strong>Notifications for free:</strong> watch a question and Confluence tells you about new answers.</li>
  <li><strong>Accepted answers and voting:</strong> the asker, or a space moderator, can accept the best answer.</li>
  <li><strong>FAQ view:</strong> solved questions in an order your moderators choose. No points or leaderboards.</li>
  <li><strong>Tags and an Unanswered queue</strong> so nothing gets lost.</li>
  <li><strong>Embed anywhere:</strong> add the Questions macro to any page, with an Ask button.</li>
  <li><strong>Your content stays yours:</strong> everything is ordinary Confluence content, so it stays if you uninstall.</li>
</ul>
<h2>Getting started</h2>
<ol>
  <li>Install the app from the Atlassian Marketplace.</li>
  <li>In a space, open <em>Space apps → Questions</em> in the sidebar and click <em>Ask a question</em>.</li>
  <li>Optional: space admins can pick moderators under <em>Space settings → Q&amp;A</em>.</li>
  <li>Optional: add the <em>Questions (Q&amp;A)</em> macro to any page.</li>
</ol>
<h2>FAQ</h2>
<p><strong>Where are questions stored?</strong> As pages under a "Questions" page in the space, with answers as comments. Votes and the accepted answer are stored as page properties.</p>
<p><strong>A new question doesn't show in the FAQ yet.</strong> Confluence search can take a few seconds to index changes.</p>
<p><strong>What happens if my subscription ends?</strong> Everything stays readable in Confluence. Asking, answering and voting through the app pause until the license is active again.</p>
<p>Questions? <a href="/support/">Contact support</a>.</p>
""")

page("recurring-issues/index.html", "Recurring Issues for Jira | Loopwise Labs",
     "Create recurring Jira issues on a schedule, in each team's time zone.", f"""
<div class="pill">Jira Cloud app</div>
<h1>Recurring Issues for Jira</h1>
<p class="lead">Daily standups, weekly reports, monthly reviews. The issues appear on time, where your team works.</p>
<ul class="features">
  <li><strong>Plain schedules:</strong> every day, every weekday, chosen weekdays, every N weeks, or monthly (including the last day). No cron.</li>
  <li><strong>Correct time zones:</strong> each rule keeps its local time across daylight saving changes.</li>
  <li><strong>Sprint-aware:</strong> new issues go straight into the active sprint, on Scrum and team-managed boards.</li>
  <li><strong>Tidy:</strong> optionally close the previous unfinished copy when a new one is created.</li>
  <li><strong>Templates:</strong> <code>{{{{date}}}}</code>, <code>{{{{weekday}}}}</code>, <code>{{{{week}}}}</code>, <code>{{{{month}}}}</code>, <code>{{{{year}}}}</code> in titles and descriptions.</li>
  <li><strong>Safe:</strong> one catch-up issue after downtime, never a flood. Runs on Atlassian, so no data leaves Atlassian.</li>
</ul>
<h2>Getting started</h2>
<ol>
  <li>Install the app from the Atlassian Marketplace.</li>
  <li>In Jira, open <em>Apps → Recurring issues</em> and click <em>New recurring issue</em>.</li>
  <li>Pick the project, issue type and schedule. The preview shows the next five runs. Save.</li>
  <li>Use <em>Run now</em> to create one immediately and check the result.</li>
</ol>
<h2>FAQ</h2>
<p><strong>Who is the reporter?</strong> The user who created the rule. If Jira doesn't allow setting the reporter, the issue is created without it instead of failing.</p>
<p><strong>The issue wasn't added to the sprint.</strong> The project needs a started sprint on a Scrum or team-managed board. The rule shows a warning when no active sprint is found.</p>
<p><strong>What happens if my subscription ends?</strong> Your rules are kept but no new issues are created until the license is active again.</p>
<p>Questions? <a href="/support/">Contact support</a>.</p>
""")

page("support/index.html", "Support | Loopwise Labs", "Get help with Loopwise Labs apps.", f"""
<h1>Support</h1>
<p class="lead">Email us and a developer will answer, usually within 2 business days.</p>
<div class="card">
  <h3><a href="mailto:{EMAIL}">{EMAIL}</a></h3>
  <p>To help us help you, please include your Atlassian site URL (e.g. <code>yourteam.atlassian.net</code>), the app name, what you expected, and what happened. A screenshot of the rule helps a lot.</p>
</div>
<p>Security issue? Write to the same address with "SECURITY" in the subject.</p>
""")

page("privacy/index.html", "Privacy Policy | Loopwise Labs", "How Loopwise Labs apps handle data.", f"""
<h1>Privacy Policy</h1>
<p class="meta">Last updated: {UPDATED}</p>
<p>This policy explains how {ENTITY}, operating under the brand Loopwise Labs ("Loopwise Labs", "we"), handles data in the Atlassian Marketplace apps <strong>Recurring Issues for Jira</strong>, <strong>Q&amp;A for Confluence</strong>, <strong>Page Approval for Confluence</strong>, <strong>Epic Progress for Jira</strong> and <strong>Issue Templates for Jira</strong> (each an "App").</p>
<h2>1. Where the App runs</h2>
<p>The App is built on Atlassian Forge and runs entirely on Atlassian's infrastructure. It does not send data to servers operated by us or by any third party.</p>
<h2>2. What the Apps store</h2>
<p><strong>Recurring Issues for Jira</strong> stores in Atlassian Forge storage, for each recurring rule your users create:</p>
<ul>
  <li>summary and description templates;</li>
  <li>project ID, issue type ID, labels and schedule (time, time zone, dates);</li>
  <li>the Atlassian account ID of the user who created the rule and, if set, of the assignee;</li>
  <li>run status: the last created issue key, timestamps and the last error message.</li>
</ul>
<p><strong>Q&amp;A for Confluence</strong> creates ordinary Confluence content on behalf of your users (questions as pages, answers as comments, labels for tags and status). In addition it stores:</p>
<ul>
  <li>in page properties: the account IDs of users who voted and of the user who accepted an answer;</li>
  <li>in Atlassian Forge storage: per space, the account IDs of moderators and the FAQ order.</li>
</ul>
<p><strong>Page Approval for Confluence</strong> stores in page properties the approval status and history of each page: the account IDs of the requester and approvers, their decisions and comments, page versions, dates and an optional note. In Atlassian Forge storage it keeps per space the account IDs of default approvers and approval managers. It also adds status labels and posts comments that @mention approvers and requesters.</p>
<p><strong>Epic Progress for Jira</strong> stores no data. It reads issues as the viewing user to show progress and keeps nothing afterwards.</p>
<p><strong>Issue Templates for Jira</strong> stores in Atlassian Forge storage the templates your users write (names, texts, issue type, priority and label names, sub-task texts) and one setting. It stores no account IDs.</p>
<p>The Apps do not store names or email addresses. Apart from Atlassian account IDs, the only personal data is free text your users choose to enter (such as approval notes and comments).</p>
<h2>3. What we can access</h2>
<p>We do not have access to your Jira or Confluence content or the Apps' stored data. The exception is function logs that Atlassian provides to app developers. These contain technical information (IDs, issue keys, error messages) and are used only to diagnose problems.</p>
<h2>4. Purpose and legal basis</h2>
<p>The data is processed only to provide the Apps' functionality, such as creating issues on the schedule you configure running questions and answers or approvals in your spaces (performance of a contract).</p>
<h2>5. Retention and deletion</h2>
<p>App data stays until it is deleted by your users or the App is uninstalled. After uninstall, Atlassian deletes the App's Forge storage under its own retention rules. Questions, answers and approval comments created by the Apps are your Confluence content and remain in your spaces until you delete them. Once a week each App asks Atlassian which stored accounts have been closed and removes those account IDs from its data.</p>
<h2>6. Sub-processors</h2>
<p>Atlassian (hosting via Forge). See the <a href="https://www.atlassian.com/legal/privacy-policy">Atlassian Privacy Policy</a>.</p>
<h2>7. Your rights</h2>
<p>Depending on your location (for example under the GDPR), you may have rights of access, correction, deletion and objection. Because the Apps store data only inside your Atlassian site, most requests can be fulfilled by deleting the relevant rules or content. Otherwise, contact us.</p>
<h2>8. Data Processing Agreement</h2>
<p>For customers subject to the GDPR, our <a href="/dpa/">Data Processing Agreement</a> applies automatically to the processing described above.</p>
<h2>9. Contact</h2>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
""")

page("dpa/index.html", "Data Processing Agreement | Loopwise Labs",
     "Data Processing Agreement for Loopwise Labs apps (GDPR Art. 28).", f"""
<h1>Data Processing Agreement</h1>
<p class="meta">Last updated: {UPDATED}</p>
<p>This Data Processing Agreement ("DPA") forms part of the <a href="/terms/">End User Terms</a> between the customer that installs the Atlassian Marketplace apps <strong>Recurring Issues for Jira</strong>, <strong>Q&amp;A for Confluence</strong>, <strong>Page Approval for Confluence</strong>, <strong>Epic Progress for Jira</strong> and <strong>Issue Templates for Jira</strong> (each an "App") ("Customer", acting as controller) and {ENTITY}, operating under the brand Loopwise Labs ("Loopwise Labs", acting as processor). It applies automatically when the Customer installs the App and Loopwise Labs processes Customer Personal Data on the Customer's behalf. No signature is required.</p>

<h2>1. Definitions</h2>
<p>"GDPR" means Regulation (EU) 2016/679, and, where applicable, the UK GDPR and the Serbian Law on Personal Data Protection. "Customer Personal Data" means personal data processed by the App on behalf of the Customer. Terms such as "controller", "processor", "data subject", "personal data breach" and "processing" have the meanings given in the GDPR.</p>

<h2>2. Details of processing</h2>
<ul>
  <li><strong>Subject matter and purpose:</strong> Recurring Issues for Jira: creating Jira issues on schedules configured by the Customer's users. Q&amp;A for Confluence: creating and organising questions and answers as Confluence content. Page Approval for Confluence: recording approval requests and decisions on Confluence pages and notifying the people involved.</li>
  <li><strong>Duration:</strong> while the App is installed, plus the deletion period in section 9.</li>
  <li><strong>Nature of processing:</strong> storage of configuration and metadata, and use of it to create, assign and transition Jira issues or to create Confluence pages, comments, labels and page properties.</li>
  <li><strong>Categories of data subjects:</strong> the Customer's Atlassian users who create rules, are set as assignees, vote, accept answers, are named moderators, request or decide approvals, or are named default approvers or approval managers.</li>
  <li><strong>Types of personal data:</strong> Atlassian account IDs, plus, for Page Approval for Confluence, the free-text notes and decision comments users enter. No names, email addresses or special categories of data are stored.</li>
</ul>

<h2>3. Processing on instructions</h2>
<p>Loopwise Labs processes Customer Personal Data only on the Customer's documented instructions, which are given through the App's configuration and these terms, unless required otherwise by law. Loopwise Labs will inform the Customer if it believes an instruction infringes data protection law.</p>

<h2>4. Confidentiality</h2>
<p>Anyone authorised by Loopwise Labs to process Customer Personal Data is bound by confidentiality.</p>

<h2>5. Security</h2>
<p>The App is built on Atlassian Forge and runs entirely on Atlassian's infrastructure. Data is stored in Atlassian-managed Forge storage, protected by Atlassian's security controls, and is not transferred to systems operated by Loopwise Labs or third parties. Loopwise Labs keeps access to production limited to what Atlassian exposes to developers (function logs, which contain no personal data beyond technical identifiers) and uses multi-factor authentication for its accounts.</p>

<h2>6. Sub-processors</h2>
<p>The Customer authorises Atlassian (Atlassian Pty Ltd and its affiliates) as sub-processor for hosting via Forge. Loopwise Labs will notify the Customer of any new sub-processor by updating this page at least 30 days in advance, giving the Customer the opportunity to object. Loopwise Labs remains responsible for its sub-processors' compliance.</p>

<h2>7. International transfers</h2>
<p>Customer Personal Data is stored by Atlassian under Atlassian's own data transfer mechanisms (including the EU Standard Contractual Clauses where applicable). Where Loopwise Labs itself accesses Customer Personal Data from the Republic of Serbia, the parties agree that the EU Standard Contractual Clauses (Module 2, controller to processor) are incorporated by reference.</p>

<h2>8. Assistance and data subject requests</h2>
<p>Loopwise Labs will assist the Customer, taking into account the nature of processing, with data subject requests, security, breach notification, data protection impact assessments and prior consultation. Because the Apps store data only inside the Customer's site, most requests can be fulfilled by the Customer deleting the relevant rules or content. Each week each App also removes account IDs of accounts that Atlassian reports as closed.</p>

<h2>9. Deletion</h2>
<p>When an App is uninstalled, its Forge storage is deleted by Atlassian under Atlassian's retention rules. Confluence content created through the Apps is the Customer's content and stays under the Customer's control. On request, Loopwise Labs will confirm deletion of any Customer Personal Data under its control.</p>

<h2>10. Personal data breaches</h2>
<p>Loopwise Labs will notify the Customer without undue delay, and in any case within 72 hours, after becoming aware of a personal data breach affecting Customer Personal Data, with the information reasonably available to it.</p>

<h2>11. Audits</h2>
<p>Loopwise Labs will make available the information necessary to demonstrate compliance with this DPA and will respond to reasonable written audit questionnaires once per year, or after a personal data breach.</p>

<h2>12. Order of precedence</h2>
<p>If this DPA conflicts with the End User Terms regarding the processing of Customer Personal Data, this DPA prevails.</p>

<h2>Contact</h2>
<p>Privacy and DPA questions: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
""")

page("terms/index.html", "End User Terms | Loopwise Labs", "Terms for using Loopwise Labs apps.", f"""
<h1>End User Terms</h1>
<p class="meta">Last updated: {UPDATED}</p>
<p>These terms are between {ENTITY}, operating under the brand Loopwise Labs ("Loopwise Labs", "we"), and the customer that installs the Atlassian Marketplace apps <strong>Recurring Issues for Jira</strong>, <strong>Q&amp;A for Confluence</strong>, <strong>Page Approval for Confluence</strong>, <strong>Epic Progress for Jira</strong> and <strong>Issue Templates for Jira</strong> (each an "App") through the Atlassian Marketplace ("you").</p>
<ol>
  <li><strong>License.</strong> While your subscription is active, we grant you a non-exclusive, non-transferable right to use the App on the Atlassian sites for which you purchased it.</li>
  <li><strong>Purchases and billing.</strong> Purchases, trials, renewals and refunds are handled by Atlassian under the Atlassian Marketplace terms.</li>
  <li><strong>Acceptable use.</strong> You may not reverse-engineer the App, resell it, or use it to break the law or Atlassian's terms.</li>
  <li><strong>Your data.</strong> You keep all rights to your data. We process it only as described in our <a href="/privacy/">Privacy Policy</a>.</li>
  <li><strong>Support.</strong> We provide support by email at <a href="mailto:{EMAIL}">{EMAIL}</a> on a reasonable-effort basis, normally within 2 business days.</li>
  <li><strong>Changes.</strong> We may update the App. We will not materially reduce its core functionality during a paid subscription term without notice.</li>
  <li><strong>Warranty disclaimer.</strong> The App is provided "as is". We do not guarantee that it is error-free or uninterrupted. It runs on Atlassian infrastructure, which we do not control.</li>
  <li><strong>Limitation of liability.</strong> To the maximum extent permitted by law, our total liability is limited to the amount you paid for the App in the 12 months before the claim. We are not liable for indirect or consequential damages.</li>
  <li><strong>Termination.</strong> These terms end when your subscription ends or you uninstall the App. Sections 4, 7, 8 and 10 survive.</li>
  <li><strong>Governing law.</strong> These terms are governed by the laws of the Republic of Serbia, and the competent court in the Republic of Serbia has jurisdiction, unless mandatory consumer law says otherwise.</li>
</ol>
""")

(ROOT / "CNAME").write_text(DOMAIN + "\n")
(ROOT / "404.html").write_text((ROOT / "index.html").read_text(encoding="utf-8"), encoding="utf-8")
print("built")
