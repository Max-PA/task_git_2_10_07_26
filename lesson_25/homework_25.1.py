# ДЗ 25.1.Робота з локаторами
#
# Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
# Використовувати функцію text(), пошук за атрибутом @, та складні локатори (більш ніж з одним елементом)
# Дані для входу на сайт -
# login - guest
# pass - welcome2qauto
# Для доступу через селеніум можна використати наступну конструкцію - driver.get("<https://UserName:Password@qauto2.forstudy.space>;");
# Сдавати у формі файлу з локаторами у гіті

#XPath локатори

# після авторизації на стороінку - https://qauto2.forstudy.space/panel/garage

# //button[text()="Add car"]
# //p[text()="You don’t have any cars in your garage"]
# //button[@id="userNavDropdown"]
# //img[@alt="User photo"]
# //a[@href="/panel/garage"]
# //app-garage//button[text()="Add car"]
# //nav[@class="sidebar d-flex flex-column"]//a[@href="/panel/garage"]
# //div[@class="main"]//app-garage//h1[text()="Garage"]
# //div[@class="panel-page_heading d-flex justify-content-between"]//button[text()="Add car"]
# //div[@class="panel-page_content"]//div[@class="panel-page_cars"]
# //div[@class="panel-page_cars"]//div[@class="panel-page_empty panel-empty"]
# //div[@class="panel-page_empty panel-empty"]//p[contains(text(), "garage")]
# //button[@id="userNavDropdown" and contains(., "My profile")]
# //footer//p[contains(text(), "Hillel IT school")]

# після авторизації на сторінку https://qauto2.forstudy.space/panel/instructions
#
# //ul[@aria-labelledby="brandSelectDropdown"]//li[text()="BMW"]
# //ul[@aria-labelledby="brandSelectDropdown"]//li[text()="Porsche"]
# //button[@id="modelSelectDropdown"]
# //ul[@aria-labelledby="modelSelectDropdown"]//li[text()="R8"]
# //button[contains(@class, "instructions-search-controls_search") and text()="Search"]
# //ul[@class="instructions_list instruction-list"]
# //ul[@class="instructions_list instruction-list"]//li
# //li[@class="instruction-list_item"]//p[contains(text(), "windshield wipers")]
# //li[@class="instruction-list_item"]//a[@class="instruction-link_download" and contains(@href, "roll bar")]
# //a[@class="instruction-link" and contains(@href, "audi/tt")]
# //a[@class="instruction-link_download"]


#CSS локатори

# https://qauto2.forstudy.space/panel/instructions
# nav.header_nav a[href="/panel/garage"]
# nav.header_nav a[href="/panel/expenses"]
# nav.header_nav a[href="/panel/instructions"]
# button#userNavDropdown
# button#userNavDropdown[aria-expanded="false"]
# nav.sidebar.d-flex.flex-column
# app-instructions
# app-instructions .panel-page_heading > h1
# div.instructions-search-controls
# button#brandSelectDropdown
# ul[aria-labelledby="brandSelectDropdown"]
# ul[aria-labelledby="brandSelectDropdown"] li.brand-select-dropdown_item
# button#modelSelectDropdown
# ul[aria-labelledby="modelSelectDropdown"] li.model-select-dropdown_item
# div.instructions-search-controls button.instructions-search-controls_search.btn-primary
# ul.instructions_list.instruction-list li.instruction-list_item a.instruction-link


# https://qauto2.forstudy.space/panel/garage
# nav.sidebar a[href="/panel/garage"]
# div.main app-garage
# app-garage .panel-page_heading > h1
# app-garage .panel-page_heading button.btn-primary
# app-garage .panel-page_content .panel-page_cars
# app-garage .panel-page_empty.panel-empty
# footer a.footer_logo
# .modal-footer > button:nth-child(2)
# app-garage .panel-page_content
# app-footer .footer_logo svg path