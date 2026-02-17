# Deep Learning

<div class="modern-typewriter">
    <span id="typewriter-text"></span>
    <span class="blinking-cursor"></span>
</div>

<style>
    /* --- 核心样式 --- */
    .modern-typewriter {
        /* 字体设置：优先使用系统现代字体 */
        font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-weight: 700;       /* 粗体，显眼但不过分 */
        font-size: 1.8rem;      /* 字号：1.8倍根字号，适中 */
        color: #2c3e50;         /* 颜色：深灰蓝，比纯黑更现代 */
        /* 如果是暗黑模式笔记，请把上面改成 color: #e0e0e0; */
        
        display: flex;
        justify-content: center; /* 居中 */
        align-items: center;
        white-space: nowrap;     /* 关键：强制不换行 */
        margin: 20px 0;          /* 上下留白 */
        line-height: 1.2;
    }

    /* --- 光标样式 --- */
    .blinking-cursor {
        display: inline-block;
        width: 3px;              /* 光标宽度 */
        height: 1.8rem;          /* 光标高度与文字一致 */
        background-color: #2c3e50; /* 光标颜色，建议与文字一致 */
        margin-left: 4px;
        animation: blink-animation 1s step-end infinite;
    }

    /* 光标闪烁动画 */
    @keyframes blink-animation {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
    }
</style>

<script>
    (function() {
        // ---在此处修改你的列表---
        const phrases = [
            "Deep Learning",
            "AlexNet",
            "ImageNet",
            "Transformer",
            "GAN"
        ];

        const el = document.getElementById("typewriter-text");
        let loopIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        
        // 速度设置 (单位: 毫秒)
        const typeSpeed = 80;    // 打字速度
        const deleteSpeed = 40;  // 删除速度
        const holdTime = 2000;   // 打完字后停留的时间

        function loop() {
            const currentPhrase = phrases[loopIndex];

            if (isDeleting) {
                // 删除逻辑
                el.innerText = currentPhrase.substring(0, charIndex - 1);
                charIndex--;
            } else {
                // 输入逻辑
                el.innerText = currentPhrase.substring(0, charIndex + 1);
                charIndex++;
            }

            // 动态决定下一次回调的时间
            let delta = isDeleting ? deleteSpeed : typeSpeed;

            if (!isDeleting && charIndex === currentPhrase.length) {
                // 打完了，停顿一会儿
                delta = holdTime;
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                // 删完了，切换到下一句
                isDeleting = false;
                loopIndex = (loopIndex + 1) % phrases.length;
                delta = 500; // 开始新句子前的小停顿
            }

            setTimeout(loop, delta);
        }

        loop();
    })();
</script>