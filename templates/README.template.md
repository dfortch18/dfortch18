{% if banner %}
![{{ banner.alt }}]({{ banner.url }})
{% endif %}

# Hi! I'm {{ name | default(username) }} 👋

{{ bio }}

---

## 🌟 About Me

{%- for item in about %}
- {{ item | replace("{email}", email) }}
{%- endfor %}

---

## 🚀 Technologies & Tools

{%- for tech in technologies %}
[![{{ tech.alt }}]({{ tech.badge }})]({{ tech.url }})
{%- endfor %}

---

## 📊 GitHub Stats

<table>
    {%- for row in stats.sections %}
    <tr>
    {%- for col in row %}
    {%- if col == "stats" %}
        <td>
            <img src="https://github-readme-stats.vercel.app/api?username={{ username }}&show_icons={{ stats.config.github_reamde_stats.stats.show_icons }}&theme={{ stats.config.github_reamde_stats.stats.theme }}" alt="{{ stats.config.github_reamde_stats.stats.alt }}" />
        </td>
    {%- elif col == "top_langs" %}
        <td>
            <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={{ username }}&layout={{ stats.config.github_reamde_stats.top_langs.layout }}&theme={{ stats.config.github_reamde_stats.top_langs.theme }}" alt="{{ stats.config.github_reamde_stats.top_langs.alt }}" />
        </td>
    {%- elif col == "trophy" %}
        <td colspan="2" align="center">
            <img align="center" width="84%" src="https://github-profile-trophy.vercel.app/?username={{ username }}&theme={{ stats.config.github_profile_trophy.theme }}&row={{ stats.config.github_profile_trophy.row }}&column={{ stats.config.github_profile_trophy.column }}&margin-h={{ stats.config.github_profile_trophy.margin_height }}&margin-w={{ stats.config.github_profile_trophy.margin_width }}" alt="{{ stats.config.github_profile_trophy.alt }}" />
        </td>
    {%- endif %}
    {%- endfor %}
    </tr>
    {%- endfor %}
</table>

---

## 🔥 Repository Pins

<table>
    {%- for i in range(0, repositories|length, 2) %}
    <tr>
    {%- for j in range(i, i + 2) %}
    {%- if j < repositories|length %}
        <td>
            <a href="https://github.com/{{ username }}/{{ repositories[j].name }}">
                <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username={{ username }}&repo={{ repositories[j].name }}&theme={{ repositories[j].theme }}" />
            </a>
        </td>
    {%- else %}
        <td></td>
    {%- endif %}
    {%- endfor %}
    </tr>
  {%- endfor %}
</table>
