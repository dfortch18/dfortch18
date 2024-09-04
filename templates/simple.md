{%- import 'templates/macros/badges.macro.md' as badge_macros -%}
{%- import 'templates/macros/github_stats.macro.md' as github_stats_macros -%}
# Hi, I'm {{ user.name }} 👋

{{ sections.description.content | safe }}

{% if sections.about %}
{{ sections.about.content | safe }}
{% endif %}

{% if sections.technologies %}
## Technologies

{%- for tech in sections.technologies.techs %}
{%- set section, key = tech.badge.split('.') -%}
{{ badge_macros.badge(badges_url, badges, section, key, sections.technologies.style, tech.url, tech.alt) }}
{%- endfor %}
{% endif %}

{% if sections.github_stats %}
<details>
    <summary><strong>Gihub Stats</strong></summary>
    {%- if sections.github_stats.stats -%}
    {%- set stats = sections.github_stats.stats -%}
    {{ github_stats_macros.user_stats(user.username, stats.theme, stats.show_icons) }}
    {%- endif -%}
    {%- if sections.github_stats.top_langs %}
    {%- set top_langs = sections.github_stats.top_langs -%}
    {{ github_stats_macros.top_langs(user.username, top_langs.theme, top_langs.layout, top_langs.show_icons) }}
    {%- endif -%}
</details>
{% endif %}