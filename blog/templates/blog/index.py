{% for p in photos %}
    <div>
        <img src="{{ p.image.url }}" />                                           
    </div>
{% endfor %}