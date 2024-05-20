// modal.js

// 打开弹窗函数
export function openModal(name, description, categories, venue, startsAt, price, ticketsLeft) {
    document.getElementById("myModal").style.display = "block";
    // 设置 Concert 的详细信息
    document.getElementById("concertName").innerText = "Name: " + name;
    document.getElementById("concertDescription").innerText = "Description: " + description;
    document.getElementById("concertCategories").innerText = "Categories: " + categories;
    document.getElementById("concertVenue").innerText = "Venue: " + venue;
    document.getElementById("concertStartsAt").innerText = "Starts At: " + startsAt;
    document.getElementById("concertPrice").innerText = "Price: " + price;
    document.getElementById("concertTicketsLeft").innerText = "Tickets Left: " + ticketsLeft;
    // 设置其他 Concert 详细信息
}

// 关闭弹窗函数
export function closeModal() {
    document.getElementById("myModal").style.display = "none";
}
