---
tags:
  - test
---

<style>
  /* 1. 卡片外层容器 */
  .blog-card-container {
    position: relative;
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 170px;
    background-color: var(--md-default-bg-color);
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 12px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    margin-bottom: 24px;
    padding: 12px; 
    box-sizing: border-box;
    transition: transform 0.2s, box-shadow 0.2s;
  }

  .blog-card-container:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    border-color: var(--md-accent-fg-color);
  }

  .blog-card-left {
    width: 220px;      
    min-width: 220px;  
    height: 100%;      
    border-radius: 8px;
    border: 1px solid rgba(0,0,0,0.05);
    overflow: hidden;
    margin-right: 20px;
  }

  .blog-card-left img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    margin: 0;
  }

  .blog-card-right {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding-right: 10px; 
  }

  .blog-card-title {
    font-size: 1.25rem;
    font-weight: bold;
    margin-bottom: 0.6rem;
    line-height: 1.3;
    color: var(--md-typeset-color);
  }

  .blog-card-desc {
    font-size: 0.95rem;
    opacity: 0.8;
    line-height: 1.6;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .blog-card-link {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 10;
  }

  .md-grid {
    max-width: 1540px;
    padding: 0 10px;
  }

  @media (max-width: 768px) {
    .blog-card-container {
      height: auto;
      flex-direction: column;
    }
    .blog-card-left {
      width: 100%;
      height: 180px;
      margin-right: 0;
      margin-bottom: 12px;
    }
  }
</style>

<div style="text-align: center; color: #8C495A; margin-bottom: 20px;">
    <span>本站已经运行</span>
    <span id="runtime_box"></span>
</div>

<script>
  function timingTime(){
    let start = '2024-10-28 00:00:00'
    let startTime = new Date(start).getTime()
    let currentTime = new Date().getTime()
    let difference = currentTime - startTime
    let m = Math.floor(difference / 1000)
    let mm = m % 60
    let f = Math.floor(m / 60)
    let ff = f % 60
    let s = Math.floor(f / 60)
    let ss = s % 24
    let day = Math.floor(s / 24)
    return day + "天" + ss + "时" + ff + "分" + mm + '秒'
  }
  setInterval(()=>{
    const target = document.getElementById('runtime_box');
    if(target) target.innerHTML = timingTime();
  }, 1000)
</script>

# Home

<div class="blog-card-container">
    <a href="/ACG/Yuri/" class="blog-card-link"></a>
    <div class="blog-card-left">
        <img src="https://lain.bgm.tv/r/400/pic/cover/l/f6/0f/604826_2XWRN.jpg" alt="Cover">
    </div>
    <div class="blog-card-right">
        <div class="blog-card-title">Yuri Anime List</div>
        <div class="blog-card-desc">
            这里收录了所有百合题材的番剧推荐与评价，点击查看详细列表与评分排行。
        </div>
    </div>
</div>

!!! info "官方文档"
    Zensical 官方网站: [https://zensical.org/](https://zensical.org/)  
    Zensical 官方文档: [https://zensical.org/docs/](https://zensical.org/docs/)

目前大概是将原本[MkDocs博客](https://www.eurekaimer.xyz/)的一些板块迁移过来了