{%- set user_stats_url = 'https://github-readme-stats.vercel.app/api' %}
{%- set top_langs_url = 'https://github-readme-stats.vercel.app/api/top-langs' %}
{%- macro user_stats(username, theme, show_icons=True, alt=None) %}
<img src="{{ user_stats_url + '?username=' + username + '&theme=' + theme + '&show_icons' + show_icons | string  }}" alt="{{ alt or 'Stats' }}" />
{%- endmacro %}
{%- macro top_langs(username, theme, layout='compact', show_icons=True, alt=None) %}
<img src="{{ top_langs_url + '?username=' + username + '&theme=' + theme + '&layout=' + layout + '&show_icons=' + show_icons | string  }}" alt="{{ alt or 'Top Langs' }}" />
{%- endmacro %}