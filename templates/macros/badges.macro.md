{%- macro badge(badges_url, badges, section, key, style, url=None, alt=None) %}
{%- set badge_data = badges[section][key] %}
{%- set badge_url = badges_url + badge_data.content + '-' + badge_data.color + '?style=' + style + '&logo=' + badge_data.logo + '&logoColor=' + badge_data.logoColor %}
{%- if url %}
[![{{ alt or badge_data.content }}]({{ badge_url }})]({{ url }})
{%- else %}
[![{{ alt or badge_data.content }}]({{ badge_url }})]({{ url }})
{%- endif %}
{%- endmacro %}