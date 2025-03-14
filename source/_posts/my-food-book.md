---
title: 我亲自下毒
sticky: 100
cover: /images/fengmian/封面.jpg
excerpt: |
  美味的秘诀是：爱！

  <div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 0;">
    <img src="/images/fengmian/封面.jpg" alt="封面" style="width: 33.333%;">
    <img src="/images/fengmian/封面.jpg" alt="封面" style="width: 33.333%;">
    <img src="/images/fengmian/封面.jpg" alt="封面" style="width: 33.333%;">
  </div>
type: ebook
categories:
  - 小GOOD食谱
---

<style>
.ebook-container {
  width: 100%;
  max-width: 1200px;
  margin: 30px auto;
  position: relative;
  user-select: none;
  font-family: 'Microsoft YaHei', 'Segoe UI', sans-serif;
}

.ebook-viewer {
  display: flex;
  justify-content: center;
  background: linear-gradient(to bottom, #f9f9f9, #e9e9e9);
  box-shadow: 0 10px 30px rgba(0,0,0,0.3);
  border-radius: 8px;
  overflow: hidden;
  position: relative;
  height: 700px;
  perspective: 1500px;
}

.ebook-page {
  width: 50%;
  height: 100%;
  background: #fff;
  padding: 0;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  transition: transform 0.3s ease;
  box-shadow: inset 0 0 30px rgba(0,0,0,0.05);
  overflow: hidden;
}

.ebook-page.left {
  border-right: 1px solid #ddd;
  box-shadow: inset -7px 0 30px -7px rgba(0,0,0,0.1);
}

.ebook-page.right {
  box-shadow: inset 7px 0 30px -7px rgba(0,0,0,0.1);
}

.ebook-page img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  display: block;
  margin: 0;
  transition: transform 0.3s ease;
}

.ebook-page .img-container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
}

.ebook-page .zoom-controls {
  position: absolute;
  bottom: 50px;
  right: 20px;
  display: flex;
  flex-direction: column;
  background: rgba(255,255,255,0.7);
  border-radius: 20px;
  padding: 5px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  z-index: 20;
}

.ebook-page .zoom-btn {
  width: 30px;
  height: 30px;
  border: none;
  background: rgba(0,0,0,0.6);
  color: white;
  font-size: 18px;
  border-radius: 50%;
  margin: 3px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.2s ease;
}

.ebook-page .zoom-btn:hover {
  background: rgba(0,0,0,0.8);
  transform: scale(1.1);
}

.ebook-page .zoom-btn:active {
  transform: scale(0.95);
}

.ebook-page .reset-btn {
  font-size: 12px;
  width: 40px;
  height: 20px;
  border-radius: 10px;
}

.ebook-page img:hover {
  transform: scale(1.02);
}

.ebook-title {
  margin-top: 20px;
  font-size: 28px;
  color: #333;
  text-align: center;
  font-weight: bold;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}

.ebook-controls {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 25px 0;
  background: rgba(0,0,0,0.05);
  padding: 15px;
  border-radius: 50px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.ebook-controls button {
  padding: 12px 25px;
  margin: 0 15px;
  background: linear-gradient(to bottom, #555, #333);
  color: white;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  transition: all 0.3s ease;
  box-shadow: 0 3px 10px rgba(0,0,0,0.2);
}

.ebook-controls button:hover {
  background: linear-gradient(to bottom, #666, #444);
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}

.ebook-controls button:active {
  transform: translateY(1px);
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.ebook-controls button:disabled {
  background: #999;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

#page-info {
  font-size: 16px;
  color: #555;
  font-weight: bold;
  padding: 0 20px;
  min-width: 150px;
  text-align: center;
}

.page-turner {
  position: absolute;
  top: 0;
  height: 100%;
  width: 50%;
  cursor: pointer;
  z-index: 10;
  transition: background-color 0.3s ease;
}

.page-turner.left {
  left: 0;
}

.page-turner.right {
  right: 0;
}

.page-turner:hover {
  background-color: rgba(0,0,0,0.02);
}

.page-turner.left:hover::after {
  content: "◄";
  position: absolute;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  color: rgba(0,0,0,0.2);
  font-size: 30px;
}

.page-turner.right:hover::after {
  content: "►";
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  color: rgba(0,0,0,0.2);
  font-size: 30px;
}

.page-number {
  position: absolute;
  bottom: 15px;
  font-size: 14px;
  color: #999;
  background: rgba(255,255,255,0.7);
  padding: 3px 10px;
  border-radius: 15px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.left .page-number {
  right: 20px;
}

.right .page-number {
  left: 20px;
}

.cover-page {
  width: 100%;
  background: linear-gradient(135deg, #f5f5f5, #fff);
  text-align: center;
  box-shadow: 0 0 50px rgba(0,0,0,0.1) inset;
}

.cover-page .img-container {
  width: 100%;
  height: 90%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 0;
  overflow: hidden;
}

.cover-page img {
  max-width: 95%;
  max-height: 95%;
  margin-bottom: 0;
  border-radius: 5px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  object-fit: contain;
  transform: scale(1.1);
  transition: transform 0.5s ease;
}

.cover-page img:hover {
  transform: scale(1.15);
}

.cover-page .ebook-title {
  font-size: 36px;
  margin-top: 20px;
  color: #222;
  text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
}

.backcover-page {
  width: 100%;
  background: linear-gradient(135deg, #f5f5f5, #fff);
  text-align: center;
  box-shadow: 0 0 50px rgba(0,0,0,0.1) inset;
}

.backcover-page .img-container {
  width: 100%;
  height: 90%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 0;
  overflow: hidden;
}

.backcover-page img {
  max-width: 95%;
  max-height: 95%;
  margin-bottom: 0;
  border-radius: 5px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  object-fit: contain;
  transform: scale(1.1);
  transition: transform 0.5s ease;
}

.backcover-page img:hover {
  transform: scale(1.15);
}

.backcover-page .ebook-title {
  font-size: 36px;
  margin-top: 20px;
  color: #222;
  text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
}

.hidden {
  display: none;
}

.page-tag {
  position: absolute;
  top: 15px;
  left: 15px;
  background-color: rgba(255, 255, 255, 0.8);
  color: #FFB800;
  font-weight: bold;
  padding: 5px 12px;
  border-radius: 15px;
  font-size: 16px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  z-index: 5;
  cursor: pointer;
  transition: all 0.3s ease;
}

.page-tag:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
  background-color: rgba(255, 255, 255, 0.95);
}

.tags-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin: 0 auto 20px;
  max-width: 1000px;
  padding: 10px;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.tag-item {
  color: #FFB800;
  font-weight: bold;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 5px 12px;
  border-radius: 15px;
  font-size: 14px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 184, 0, 0.3);
}

.tag-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  background-color: rgba(255, 255, 255, 0.95);
  border-color: #FFB800;
}

.hits-info {
  text-align: center;
  color: #999;
  font-size: 12px;
  margin-bottom: 15px;
}

.category {
  color: #FFB800;
}

@media (max-width: 768px) {
  .ebook-viewer {
    height: 500px;
  }
  
  .ebook-page img {
    max-width: 90%;
  }
  
  .ebook-controls button {
    padding: 10px 15px;
    font-size: 14px;
  }
}
</style>

<div class="ebook-container">
  <div class="tags-container" id="tags-container">
    <!-- 标签将通过JavaScript动态添加 -->
  </div>
  
  <div class="ebook-viewer" id="ebook-viewer">
    <!-- 页面将通过JavaScript动态添加 -->
  </div>
  
  <div class="ebook-controls">
    <button id="prev-btn">上一页</button>
    <span id="page-info">第 1-2 页 / 共 37 页</span>
    <button id="next-btn">下一页</button>
  </div>
  

</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // 页面数据
  const pages = [
    { type: 'cover', content: '<div class="img-container"><img src="/images/shipu/1.jpg" alt="封面" style="transform: scale(1.2); transition: transform 0.5s ease;"></div><h2 class="ebook-title">小GOOD私厨</h2>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/2.jpg" alt="食谱2"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/3.jpg" alt="食谱3"><div class="page-tag">早点</div></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/4.jpg" alt="食谱4"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/5.jpg" alt="食谱5"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/6.jpg" alt="食谱6"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/7.jpg" alt="食谱7"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/8.jpg" alt="食谱8"><div class="page-tag">凉菜</div></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/9.jpg" alt="食谱9"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/10.jpg" alt="食谱10"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/11.jpg" alt="食谱11"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/12.jpg" alt="食谱12"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/13.jpg" alt="食谱13"><div class="page-tag">海鲜</div></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/14.jpg" alt="食谱14"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/15.jpg" alt="食谱15"><div class="page-tag">小炒</div></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/16.jpg" alt="食谱16"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/17.jpg" alt="食谱17"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/18.jpg" alt="食谱18"><div class="page-tag">蔬菜</div></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/19.jpg" alt="食谱19"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/20.jpg" alt="食谱20"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/21.jpg" alt="食谱21"><div class="page-tag">小孩の最爱</div></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/22.jpg" alt="食谱22"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/23.jpg" alt="食谱23"><div class="page-tag">汤品</div></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/24.jpg" alt="食谱24"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/25.jpg" alt="食谱25"><div class="page-tag">夜宵搭档</div></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/26.jpg" alt="食谱26"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/27.jpg" alt="食谱27"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/28.jpg" alt="食谱28"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/29.jpg" alt="食谱29"><div class="page-tag">主食</div></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/30.jpg" alt="食谱30"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/31.jpg" alt="食谱31"><div class="page-tag">特调</div></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/32.jpg" alt="食谱32"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/33.jpg" alt="食谱33"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/34.jpg" alt="食谱34"></div>' },
    { type: 'image', content: '<div class="img-container"><img src="/images/shipu/35.jpg" alt="食谱35"></div>' },
    { type: 'backcover', content: '<div class="img-container"><img src="/images/shipu/36.jpg" alt="底面" style="transform: scale(1.2); transition: transform 0.5s ease;"></div>' }
  ];
  
  const viewer = document.getElementById('ebook-viewer');
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');
  const pageInfo = document.getElementById('page-info');
  
  let currentSpread = 0; // 当前展开的页面索引（左页的索引）
  const totalPages = pages.length;
  
  // 添加跳转功能
  function setupTagJumps() {
    const tagMap = {
      '早点': 2,
      '凉菜': 7,
      '海鲜': 12,
      '小炒': 14,
      '蔬菜': 17,
      '小孩の最爱': 20,
      '汤品': 22,
      '夜宵搭档': 24,
      '主食': 28,
      '甜点&饮料': 30,
      '成人特调(特大误)': 32
    };
    
    // 添加底部标签
    const tagsContainer = document.getElementById('tags-container');
    
    // 添加标签项
    for (const [tag, pageNum] of Object.entries(tagMap)) {
      const tagItem = document.createElement('div');
      tagItem.textContent = tag;
      tagItem.className = 'tag-item';
      
      tagItem.addEventListener('click', function() {
        // 计算要跳转到的spread索引
        const targetSpread = Math.ceil(pageNum / 2);
        currentSpread = targetSpread;
        renderSpread(currentSpread);
        
        // 滚动到查看器位置
        viewer.scrollIntoView({ behavior: 'smooth' });
      });
      
      tagsContainer.appendChild(tagItem);
    }
    
    // 点击页面标签时跳转
    document.querySelectorAll('.page-tag').forEach(tag => {
      tag.addEventListener('click', function() {
        const tagText = this.textContent;
        if (tagMap[tagText]) {
          const targetSpread = Math.ceil(tagMap[tagText] / 2);
          currentSpread = targetSpread;
          renderSpread(currentSpread);
        }
      });
    });
  }
  
  // 初始化电子书
  function initEbook() {
    // 添加点击区域用于翻页
    const leftTurner = document.createElement('div');
    leftTurner.className = 'page-turner left';
    leftTurner.addEventListener('click', prevPage);
    
    const rightTurner = document.createElement('div');
    rightTurner.className = 'page-turner right';
    rightTurner.addEventListener('click', nextPage);
    
    viewer.appendChild(leftTurner);
    viewer.appendChild(rightTurner);
    
    // 显示第一个跨页
    renderSpread(currentSpread);
    
    // 设置标签跳转
    setupTagJumps();
    
    // 按钮事件
    prevBtn.addEventListener('click', prevPage);
    nextBtn.addEventListener('click', nextPage);
    
    // 键盘事件
    document.addEventListener('keydown', function(e) {
      if (e.key === 'ArrowLeft') {
        prevPage();
      } else if (e.key === 'ArrowRight') {
        nextPage();
      }
    });
    
    // 添加触摸滑动支持
    let touchStartX = 0;
    let touchEndX = 0;
    
    viewer.addEventListener('touchstart', function(e) {
      touchStartX = e.changedTouches[0].screenX;
    }, false);
    
    viewer.addEventListener('touchend', function(e) {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    }, false);
    
    function handleSwipe() {
      if (touchEndX < touchStartX - 50) {
        // 向左滑动
        nextPage();
      } else if (touchEndX > touchStartX + 50) {
        // 向右滑动
        prevPage();
      }
    }
  }
  
  // 渲染当前跨页
  function renderSpread(spreadIndex) {
    // 清空查看器，但保留翻页区域
    const leftTurner = viewer.querySelector('.page-turner.left');
    const rightTurner = viewer.querySelector('.page-turner.right');
    
    viewer.innerHTML = '';
    
    if (leftTurner && rightTurner) {
      viewer.appendChild(leftTurner);
      viewer.appendChild(rightTurner);
    }
    
    // 特殊处理封面和封底
    if (spreadIndex === 0) {
      // 封面单独显示
      const coverPage = document.createElement('div');
      coverPage.className = 'ebook-page cover-page';
      coverPage.innerHTML = pages[0].content;
      
      // 添加缩放控制
      addZoomControls(coverPage, true);
      
      // 添加特殊的初始缩放效果
      const coverImg = coverPage.querySelector('img');
      if (coverImg) {
        setTimeout(() => {
          coverImg.style.transform = 'scale(1.2)';
        }, 100);
      }
      
      viewer.appendChild(coverPage);
      
      updatePageInfo(1, 1);
    } else if (spreadIndex * 2 >= totalPages - 1) {
      // 封底单独显示
      const backcoverPage = document.createElement('div');
      backcoverPage.className = 'ebook-page backcover-page';
      backcoverPage.innerHTML = pages[totalPages - 1].content;
      
      // 添加缩放控制
      addZoomControls(backcoverPage, true);
      
      // 添加特殊的初始缩放效果
      const backcoverImg = backcoverPage.querySelector('img');
      if (backcoverImg) {
        setTimeout(() => {
          backcoverImg.style.transform = 'scale(1.2)';
        }, 100);
      }
      
      viewer.appendChild(backcoverPage);
      
      updatePageInfo(totalPages, totalPages);
    } else {
      // 正常双页显示
      const leftIndex = spreadIndex * 2 - 1;
      const rightIndex = leftIndex + 1;
      
      // 左页
      if (leftIndex < totalPages) {
        const leftPage = document.createElement('div');
        leftPage.className = 'ebook-page left';
        leftPage.innerHTML = pages[leftIndex].content;
        leftPage.innerHTML += `<div class="page-number">${leftIndex + 1}</div>`;
        
        // 添加缩放控制
        addZoomControls(leftPage);
        
        viewer.appendChild(leftPage);
      }
      
      // 右页
      if (rightIndex < totalPages - 1) {
        const rightPage = document.createElement('div');
        rightPage.className = 'ebook-page right';
        rightPage.innerHTML = pages[rightIndex].content;
        rightPage.innerHTML += `<div class="page-number">${rightIndex + 1}</div>`;
        
        // 添加缩放控制
        addZoomControls(rightPage);
        
        viewer.appendChild(rightPage);
      }
      
      updatePageInfo(leftIndex + 1, Math.min(rightIndex + 1, totalPages - 1));
    }
    
    // 更新按钮状态
    prevBtn.disabled = (spreadIndex === 0);
    nextBtn.disabled = (spreadIndex * 2 + 1 >= totalPages);
    
    // 添加翻页动画效果
    const pageElements = document.querySelectorAll('.ebook-page');
    pageElements.forEach(page => {
      page.style.opacity = 0;
      setTimeout(() => {
        page.style.opacity = 1;
        page.style.transition = 'opacity 0.3s ease';
      }, 50);
    });
  }
  
  // 更新页码信息
  function updatePageInfo(leftPage, rightPage) {
    if (leftPage === rightPage) {
      pageInfo.textContent = `第 ${leftPage} 页 / 共 ${totalPages} 页`;
    } else {
      pageInfo.textContent = `第 ${leftPage}-${rightPage} 页 / 共 ${totalPages} 页`;
    }
  }
  
  // 上一页
  function prevPage() {
    if (currentSpread > 0) {
      currentSpread--;
      renderSpread(currentSpread);
    }
  }
  
  // 下一页
  function nextPage() {
    const maxSpread = Math.ceil((totalPages - 1) / 2);
    if (currentSpread < maxSpread) {
      currentSpread++;
      renderSpread(currentSpread);
    }
  }
  
  // 添加缩放控制功能
  function addZoomControls(pageElement, isSpecialPage = false) {
    const imgContainer = pageElement.querySelector('.img-container');
    const img = imgContainer ? imgContainer.querySelector('img') : null;
    
    if (!img) return;
    
    // 创建缩放控制按钮
    const zoomControls = document.createElement('div');
    zoomControls.className = 'zoom-controls';
    zoomControls.innerHTML = `
      <button class="zoom-btn zoom-in">+</button>
      <button class="zoom-btn zoom-out">-</button>
      <button class="zoom-btn reset-btn">重置</button>
    `;
    
    pageElement.appendChild(zoomControls);
    
    // 设置初始缩放和位置
    let scale = isSpecialPage ? 1.5 : 1;
    let posX = 0;
    let posY = 0;
    let isDragging = false;
    let startX, startY, startPosX, startPosY;
    
    // 更新图片变换
    function updateTransform() {
      img.style.transform = `scale(${scale}) translate(${posX}px, ${posY}px)`;
    }
    
    // 初始应用变换
    updateTransform();
    
    // 缩放按钮事件
    const zoomIn = zoomControls.querySelector('.zoom-in');
    const zoomOut = zoomControls.querySelector('.zoom-out');
    const resetBtn = zoomControls.querySelector('.reset-btn');
    
    zoomIn.addEventListener('click', function(e) {
      e.stopPropagation();
      scale = Math.min(scale + 0.2, 3);
      updateTransform();
    });
    
    zoomOut.addEventListener('click', function(e) {
      e.stopPropagation();
      scale = Math.max(scale - 0.2, 0.5);
      updateTransform();
    });
    
    resetBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      scale = 1;
      posX = 0;
      posY = 0;
      updateTransform();
    });
    
    // 拖动图片功能
    img.addEventListener('mousedown', function(e) {
      if (scale > 1) {
        isDragging = true;
        startX = e.clientX;
        startY = e.clientY;
        startPosX = posX;
        startPosY = posY;
        img.style.cursor = 'grabbing';
        e.preventDefault();
      }
    });
    
    document.addEventListener('mousemove', function(e) {
      if (isDragging) {
        const dx = (e.clientX - startX) / scale;
        const dy = (e.clientY - startY) / scale;
        posX = startPosX + dx;
        posY = startPosY + dy;
        updateTransform();
      }
    });
    
    document.addEventListener('mouseup', function() {
      isDragging = false;
      img.style.cursor = 'grab';
    });
    
    // 鼠标滚轮缩放
    imgContainer.addEventListener('wheel', function(e) {
      e.preventDefault();
      const delta = e.deltaY > 0 ? -0.1 : 0.1;
      scale = Math.max(0.5, Math.min(scale + delta, 3));
      updateTransform();
    });
    
    // 双击重置
    img.addEventListener('dblclick', function() {
      if (scale === 1) {
        scale = 2;
      } else {
        scale = 1;
        posX = 0;
        posY = 0;
      }
      updateTransform();
    });
    
    // 设置初始样式
    img.style.cursor = 'grab';
    img.style.transform = 'scale(1)';
    img.style.transformOrigin = 'center center';
  }
  
  // 初始化
  initEbook();
});
</script>
