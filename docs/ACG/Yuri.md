# Yuri Rank

<div class="sort-container">
    <label for="sortOrder">全站排序方式：</label>
    <select id="sortOrder" class="sort-select" onchange="handleSortChange(this)">
        <option value="desc">按年份：从新到旧</option>
        <option value="asc">按年份：从旧到新</option>
    </select>
</div>

!!! info "声明"
    这里的百合包含了所谓的轻百合和重百合，因为题材原因和时代局限性，我认为有许多作品都有暧昧不清的定位问题

<h2>番剧</h2>
<div class="anime-grid" id="animeGrid"></div>

<h2>漫画</h2>
<div class="anime-grid" id="mangaGrid"></div>

<h2>小说</h2>
<div class="anime-grid" id="novelGrid"></div>

<div class="anime-grid" id="animeGrid"></div>

<script>

const animeData = [
    {
        title: "超时空辉夜姬",
        year: 2026,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/f6/0f/604826_2XWRN.jpg",
        review: "剧情或许有瑕疵，但是作画和特效已经杀穿了，百合番最富裕的一仗"  
    },
    {
        title: "莉兹与青鸟",
        year: 2018,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/1d/35/216371_5926R.jpg",
        review: "明暗双线相互成全，音乐和演出双重神话，同为莉兹，互为青鸟，精美清新的童话故事，山田尚子的巅峰之作"
    },
    {
        title: "安达与岛村",
        year: 2020,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/0f/a4/282372_ZzaMQ.jpg",
        review: "百合界最长的河，入间人间最优秀的纯爱百合小说改编，但是动漫展现力还是相对较差(中庸级别)"
    },
    {
        title: "转生公主与天才千金的魔法革命",
        year: 2023,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/fd/3c/395714_5EeZx.jpg",
        review: "这部的动画表现力是可以的(给自己拐个1回家的故事)，但是原著小说后期下滑了(水魔法还是值得一看的)，但是估计没有第二季了"
    },
    {
        title: "终将成为妳",
        year: 2018,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/bc/72/243981_J20I2.jpg",
        review: "百合最高的山，最长的河，无可争议的百合神作，开创后终将时代的里程碑，拥有丰富内核的作品！"
    },
    {
        title: "citrus～柑橘味香气～",
        year: 2018,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/8e/45/198098_g44Mz.jpg",
        review: "橘味的起源，大多数人的评价是很雷，但是我认为还是可圈可点的，最后一集的小熊吻是不错的，但是关系混乱确实是一个雷点"
    },
    {
        title: "白箱",
        year: 2014,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/73/26/110467_Fx9tT.jpg",
        review: "基本神作，题材新颖制作精良，也是给我补充了很多动画制作的基本知识了，但是是比较轻的百合"
    },
    {
        title: "轻音少女 剧场版",
        year: 2011,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/9e/3c/12426_vt490.jpg",
        review: "无需多言，KON伟大，即便是2011年的作品依然感觉到诚意满满"
    },
    {
        title: "玉响～毕业写真～",
        year: 2015,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/2b/30/109869_w5vOo.jpg",
        review: "4集，其实感觉到是比较好的作品，但是讨论度很低"
    },
    {
        title: "玉响～more aggressive～",
        year: 2013,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/26/f9/45213_yA97f.jpg",
        review: "是比较好的作品，但是讨论度很低"
    },
    {
        title: "摇曳百合",
        year: 2011,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/43/d9/14588_bDB2r.jpg",
        review: "很经典的作品，基本四人两对，里面有个阴暗系幽灵学姐我相当喜欢"
    },
    {
        title: "摇曳百合♪♪ ",
        year: 2012,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/f2/9f/28900_PB3pC.jpg",
        review: "S2"
    },
    {
        title: "摇曳百合 3☆High!",
        year: 2015,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/3e/f2/127573_HfPRJ.jpg",
        review: "S3"
    },
    {
        title: "我们不可能成为恋人！绝对不行。 (※似乎可行？) ",
        year: 2025,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/ae/03/524707_1quxk.jpg",
        review: "莫名在2025年爆火的百合后宫题材，感觉有点莫名其妙的，原作小说和漫画都是比较出色的，动画基本上维持了一定的作画水平"
    },
    {
        title: "GIRLS BAND CRY",
        year: 2024,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/75/c1/431767_bX7FZ.jpg",
        review: "近年来少女乐队题材我心中的真正GOAT，向命运发出呐喊的歌声，真正真实的矛盾的对立冲突，风格正中我的好球区，3D和作画及其强大"
    },
    {
        title: "街角魔族",
        year: 2019,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/af/22/272510_BZ00p.jpg",
        review: "还算比较有趣的沙雕搞笑日常百合番剧"
    },
    {
        title: "亲吻那片花瓣 「恋人的羁绊」",
        year: 2010,
        img: "https://bangumi.tv/img/no_icon_subject.png",
        review: "OVA，我宣布这就是簧片啊"
    },
    {
        title: "和机器人啪啪啪能算在经验次数里吗？？",
        year: 2026,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/f0/78/558296_W25j2.jpg",
        review: "那不就是玩机器吗(bushi)，标题取胜"
    },
    {
        title: "对我垂涎欲滴的非人少女",
        year: 2025,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/2c/af/520842_J06fL.jpg",
        review: "还可以只能说，但是依旧百合番不如原作定律"
    },
    {
        title: "街角魔族 2丁目",
        year: 2022,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/ef/d3/313852_550li.jpg",
        review: "有一些比较不错的改变，虽然我不觉得这个作画和剧情有什么进步，过度的章节"
    },
    {
        title: "樱Trick",
        year: 2014,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/1c/2f/80838_pAzJ7.jpg",
        review: "开创樱t学习法，KissKiss，名句高发"
    },
    {
        title: "紫罗兰永恒花园 外传 - 永远与自动手记人偶",
        year: 2019,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/f0/15/280837_L6VeG.jpg",
        review: "有点想要搞事情的演出，很多地方单看感觉表现的像姬片，但是后续emm，建议把全部内容看完(我不剧透)"
    },
    {
        title: "恋语轻唱",
        year: 2024,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/8e/05/415166_rCv5N.jpg",
        review: "我说不好，我不好说，看原作吧，谢谢(读到这里请为竹岛老师哀悼三分钟)"
    },
];

// 2. 漫画数据 (在这里填写漫画)
const mangaData = [
    {
        title: "温热的银莲花",
        year: 2021,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/70/4e/326868_k828Z.jpg",
        review: "画风极其精美，情感细腻，虽然是韩漫但是分镜非常有张力"
    },
    {
        title: "也就是一般的百合酱",
        year: 2019,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/54/a8/275369_w0820.jpg",
        review: "非常轻松可爱的日常百合，看着会让人露出姨母笑"
    }
];

// 3. 小说数据 (在这里填写小说)
const novelData = [
    {
        title: "关于佐伯沙弥香",
        year: 2018,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/34/4e/266205_5z4zL.jpg",
        review: "入间人间执笔的终将外传，补完了沙弥香的过去与未来，文笔极佳"
    },
    {
        title: "女性向游戏女主角...",
        year: 2018,
        img: "https://lain.bgm.tv/r/400/pic/cover/l/79/11/269661_8x8X9.jpg",
        review: "转生恶役流的经典之作，虽然是轻小说但是百合度很高"
    }
];

// 通用渲染函数：指定数据渲染到指定ID的容器中
function renderGrid(data, containerId) {
    const grid = document.getElementById(containerId);
    if (!grid) return; // 如果找不到容器就跳过
    
    grid.innerHTML = ''; // 清空当前内容
    
    data.forEach(item => {
        const cardHTML = `
            <div class="anime-card" data-year="${item.year}">
                <div class="poster-wrapper">
                    <img src="${item.img}" loading="lazy" alt="${item.title}">
                    <div class="review-overlay">
                        ${item.review}
                    </div>
                </div>
                <div class="anime-info">
                    <span class="anime-title">${item.title}</span>
                    <span class="anime-year">${item.year}</span>
                </div>
            </div>
        `;
        grid.insertAdjacentHTML('beforeend', cardHTML);
    });
}

// 通用排序函数：对数据进行排序
function getSortedData(data, order) {
    // 复制一份数据以免修改原数组
    return [...data].sort((a, b) => {
        return order === 'desc' ? b.year - a.year : a.year - b.year;
    });
}

// 总控制器：同时刷新三个板块
function refreshAllGrids(order) {
    // 1. 渲染番剧
    renderGrid(getSortedData(animeData, order), 'animeGrid');
    // 2. 渲染漫画
    renderGrid(getSortedData(mangaData, order), 'mangaGrid');
    // 3. 渲染小说
    renderGrid(getSortedData(novelData, order), 'novelGrid');
}

// 监听下拉菜单变化
function handleSortChange(selectElement) {
    refreshAllGrids(selectElement.value);
}

// 页面加载完成后，默认执行一次降序排列
document.addEventListener('DOMContentLoaded', () => refreshAllGrids('desc'));
</script>