# Yuri Rank

<div class="sort-container">
    <label for="sortOrder">排序方式：</label>
    <select id="sortOrder" class="sort-select" onchange="handleSortChange(this)">
        <option value="desc">按年份：从新到旧</option>
        <option value="asc">按年份：从旧到新</option>
    </select>
</div>

<div class="anime-grid" id="animeGrid">
    <div class="anime-card" data-year="2026">
        <div class="poster-wrapper">
            <img src="https://lain.bgm.tv/r/400/pic/cover/l/f6/0f/604826_2XWRN.jpg" loading="lazy">
            <div class="review-overlay">
                剧情或许有瑕疵，但是作画和特效已经杀穿了，百合番最富裕的一仗
            </div>
        </div>
        <div class="anime-info">
            <span class="anime-title">超时空辉夜姬</span>
            <span class="anime-year">2026</span>
        </div>
    </div>
</div>

<script>
function handleSortChange(selectElement) {
    sortAnime(selectElement.value);
}

function sortAnime(order) {
    const grid = document.getElementById('animeGrid');
    const cards = Array.from(grid.getElementsByClassName('anime-card'));
    cards.sort((a, b) => {
        const yearA = parseInt(a.getAttribute('data-year'));
        const yearB = parseInt(b.getAttribute('data-year'));
        return order === 'desc' ? yearB - yearA : yearA - yearB;
    });
    cards.forEach(card => grid.appendChild(card));
}

document.addEventListener('DOMContentLoaded', () => sortAnime('desc'));
</script>