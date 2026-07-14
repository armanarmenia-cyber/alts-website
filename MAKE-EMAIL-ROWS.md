# Строки для шаблона письма в Make

Вставить в HTML-тело письма (внутрь `<table>`). Плейсхолдеры `{{...}}` заменить чипами из панели маппинга (кликом, не текстом!). Пустые поля просто останутся пустыми.

## Full-buyer (анкета)

```html
<tr><td><b>City</b></td><td>{{city}}</td></tr>
<tr><td><b>Country</b></td><td>{{country}}</td></tr>
<tr><td><b>Description</b></td><td>{{description}}</td></tr>
<tr><td><b>Business started</b></td><td>{{business_started}}</td></tr>
<tr><td><b>Business type</b></td><td>{{business_type}}</td></tr>
<tr><td><b>Employees</b></td><td>{{employees}}</td></tr>
<tr><td><b>Client spend / night</b></td><td>{{client_spend}}</td></tr>
<tr><td><b>Bookings turnover</b></td><td>{{turnover}}</td></tr>
<tr><td><b>5* share</b></td><td>{{five_star_share}}</td></tr>
<tr><td><b>Consortia</b></td><td>{{consortia}}</td></tr>
<tr><td><b>Trade shows (as buyer)</b></td><td>{{trade_shows}}</td></tr>
<tr><td><b>Regions</b></td><td>{{regions}}</td></tr>
<tr><td><b>Products</b></td><td>{{products}}</td></tr>
<tr><td><b>Clients based</b></td><td>{{clients_based}}</td></tr>
<tr><td><b>Top-3 hotels</b></td><td>{{top_hotels}}</td></tr>
<tr><td><b>Recent bookings</b></td><td>{{recent_bookings}}</td></tr>
```

## Full-exhibitor (пакеты, инвойс, материалы)

```html
<tr><td><b>Package Baltic</b></td><td>{{package_baltic}}</td></tr>
<tr><td><b>Package Lisbon</b></td><td>{{package_lisbon}}</td></tr>
<tr><td><b>Lisbon extras</b></td><td>{{extras_lisbon}}</td></tr>
<tr><td><b>Package Warsaw</b></td><td>{{package_warsaw}}</td></tr>
<tr><td><b>Warsaw extras</b></td><td>{{extras_warsaw}}</td></tr>
<tr><td><b>Legal name</b></td><td>{{legal_name}}</td></tr>
<tr><td><b>VAT</b></td><td>{{vat}}</td></tr>
<tr><td><b>Invoice address</b></td><td>{{invoice_address}}</td></tr>
<tr><td><b>2nd attendee</b></td><td>{{attendee2}}</td></tr>
<tr><td><b>Catalogue entry</b></td><td>{{catalogue}}</td></tr>
<tr><td><b>Materials link</b></td><td>{{materials}}</td></tr>
```

Поле `question` (полный текстовый отчёт) можно оставить в письме как резервную сводку или удалить строку — данные теперь дублируются в отдельных полях.
