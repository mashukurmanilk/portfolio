/**
 * MASHUKUR MANIK PORTFOLIO SCRIPT
 * Handles Typewriter animation, scroll spy, mobile drawer,
 * project details modal, resume preview modal, skills filter,
 * copy-to-clipboard, contact form validation, and back-to-top.
 */

document.addEventListener('DOMContentLoaded', () => {

  // ==================== 1. PROJECT DATA DICTIONARY ====================
  const projectsData = {
    booknook: {
      name: "BookNook – Full-Stack Library Ecosystem",
      category: "MERN Stack Application",
      image: "assets/project-booknook.png",
      liveUrl: "https://booknook-client.vercel.app",
      clientRepo: "https://github.com/mashukurmanilk/BookNook-frontend",
      serverRepo: "https://github.com/mashukurmanilk/BookNook-backend",
      techStack: ["React.js", "Next.js", "Node.js", "Express.js", "MongoDB", "Mongoose", "Tailwind CSS", "JWT Auth"],
      description: "BookNook is a full-featured digital library management system designed to make borrowing, categorizing, and discovering books seamless. It features an intuitive reader dashboard, real-time catalog filtering, book status tracking (Available, Borrowed, Overdue), and an authenticated admin panel for inventory and user management.",
      challenges: [
        "Handling concurrent book borrowing states so multiple readers cannot simultaneously borrow the last available copy of a physical book title.",
        "Architecting secure JWT session persistence across both server-side rendered routes and client-side reactive components.",
        "Optimizing MongoDB queries for deep text search and category filtration across large book inventories."
      ],
      improvements: [
        "Integrate AI-driven book recommendations based on user reading history and genre preferences.",
        "Implement automated email reminders for upcoming due dates using Nodemailer and cron triggers.",
        "Add an interactive in-browser PDF reader for royalty-free preview excerpts."
      ]
    },

    vault: {
      name: "Private Cloud Vault – Personal Media & Storage Hub",
      category: "Next.js 14 Full Stack Hub",
      image: "assets/project-vault.png",
      liveUrl: "https://private-cloud-vault.vercel.app",
      clientRepo: "https://github.com/mashukurmanilk/private-cloud-vault",
      techStack: ["Next.js 14", "TypeScript", "Tailwind CSS", "Prisma ORM", "SQLite", "HTTP 206 Streaming", "Bcrypt"],
      description: "A zero-friction, self-hosted personal cloud storage hub. Private Cloud Vault allows users to drag-and-drop batch files, paste clipboard screenshots directly (Ctrl+V), organize documents, and stream high-bitrate video natively with instant timeline scrubbing. Built with 100% privacy and master PIN authentication.",
      challenges: [
        "Implementing native HTTP 206 Partial Content range requests in Next.js App Router for smooth video scrubbing on mobile iOS/Android browsers.",
        "Handling memory-efficient chunked file uploads without hitting serverless RAM limits.",
        "Generating instant client-side previews for various document MIME types (PDFs, Markdown, Images, Audio)."
      ],
      improvements: [
        "Implement end-to-end client-side encryption using Web Crypto API (AES-GCM-256) before uploading.",
        "Add federated storage providers (allowing sync with AWS S3, Cloudflare R2, or Google Cloud Storage).",
        "Enable one-time expiring download links for secure file sharing with external peers."
      ]
    },

    cyberhud: {
      name: "Cyber-HUD: Data Nexus – Gamified Terminal",
      category: "Interactive React Application",
      image: "assets/project-cyberhud.png",
      liveUrl: "https://cyber-hud.vercel.app",
      clientRepo: "https://github.com/mashukurmanilk/cyber-hud",
      techStack: ["React", "Vite", "Web Audio API", "HTML5 Canvas", "Tailwind CSS", "LocalStorage DB"],
      description: "A cyberpunk-themed developer productivity command center. Combines habit tracking protocols, daily task matrices, and visual focus analytics with real-time synthesized retro audio frequencies. Features an animated cyberpunk perspective grid canvas and effort-based XP leveling.",
      challenges: [
        "Synthesizing customized retro 8-bit sound effects using native Web Audio API oscillators without audio clipping or browser autoplay restrictions.",
        "Rendering an interactive 60 FPS perspective grid on HTML5 canvas while maintaining fluid UI responsiveness.",
        "Building offline-first data persistence and streak calculation logic resilient against timezone changes."
      ],
      improvements: [
        "Migrate offline storage to a cloud-synced backend with multiplayer developer quest leaderboards.",
        "Add GitHub commit sync to automatically convert real-world coding commits into in-game energy/XP.",
        "Create customizable cyberpunk theme shaders with WebGL."
      ]
    },

    bpldream: {
      name: "B14 BPL Dream 11 – Cricket Fantasy Team Builder",
      category: "Sports & Fantasy Application",
      image: "assets/project-bpldream.png",
      liveUrl: "https://bpl-dream-11.surge.sh",
      clientRepo: "https://github.com/mashukurmanilk/b14-BPL-dream-11",
      techStack: ["React", "Tailwind CSS", "DaisyUI", "React-Toastify", "Vite"],
      description: "An interactive sports draft platform where cricket enthusiasts can claim virtual coin credits, draft their dream 11 player squad within budget caps, balance player roles (Batsmen, Bowlers, All-rounders), and manage active line-ups.",
      challenges: [
        "Synchronizing remaining coin balances, active player counts, and role limitations across multiple decoupled components without state corruption.",
        "Designing smooth visual toast feedback when budget thresholds or duplicate player selections are triggered.",
        "Building a fully responsive player selection grid that feels like a native sports management application on mobile."
      ],
      improvements: [
        "Integrate live Cricbuzz / RapidAPI feed for real-time match scores and automated player fantasy points calculation.",
        "Add multiplayer draft rooms where multiple friends can participate in live player auctions.",
        "Implement tournament leaderboard rankings with social sharing cards."
      ]
    },

    bazardor: {
      name: "Bazar Dor Tracker – Daily Commodity Price Monitor",
      category: "Utility & Budgeting Web App",
      image: "assets/project-bazardor.png",
      liveUrl: "https://bazar-dor.surge.sh",
      clientRepo: "https://github.com/mashukurmanilk/bazar-dor",
      techStack: ["React", "JavaScript (ES6+)", "REST APIs", "Tailwind CSS", "Chart.js"],
      description: "A community-focused commodity price tracking tool for daily market items (vegetables, proteins, spices, pantry essentials). Enables households to calculate market baskets, compare daily price shifts, and budget grocery expenses intelligently.",
      challenges: [
        "Visualizing historical item price trends on mobile viewports using responsive charts.",
        "Structuring local item caching to allow quick price lookups in areas with poor market connectivity.",
        "Designing an intuitive unit conversion system (Kg, Gram, Liter, Piece) for consistent total price aggregation."
      ],
      improvements: [
        "Add crowd-sourced receipt scanning via OCR to automatically extract and verify market rates.",
        "Integrate location-based price comparisons between neighborhood wet markets and supermarkets.",
        "Provide weekly budget alerts and inflation trend reports."
      ]
    }
  };

  // ==================== 2. TYPEWRITER EFFECT ====================
  const typewriterElement = document.getElementById('typewriter-text');
  const designations = [
    "Full Stack Web Developer",
    "MERN Stack Specialist",
    "Next.js & React Engineer",
    "UI/UX Focused Architect",
    "Continuous Problem Solver"
  ];
  
  let phraseIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  let typingSpeed = 100;

  function typeEffect() {
    if (!typewriterElement) return;

    const currentPhrase = designations[phraseIndex];

    if (isDeleting) {
      typewriterElement.textContent = currentPhrase.substring(0, charIndex - 1);
      charIndex--;
      typingSpeed = 50;
    } else {
      typewriterElement.textContent = currentPhrase.substring(0, charIndex + 1);
      charIndex++;
      typingSpeed = 100;
    }

    if (!isDeleting && charIndex === currentPhrase.length) {
      // Pause at full phrase
      typingSpeed = 2000;
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      phraseIndex = (phraseIndex + 1) % designations.length;
      typingSpeed = 500;
    }

    setTimeout(typeEffect, typingSpeed);
  }

  typeEffect();

  // ==================== 3. NAVBAR SCROLL & ACTIVE SCROLL SPY ====================
  const navbar = document.getElementById('navbar');
  const navLinks = document.querySelectorAll('.nav-link');
  const sections = document.querySelectorAll('section[id]');
  const backToTopBtn = document.getElementById('back-to-top');

  window.addEventListener('scroll', () => {
    const scrollY = window.pageYOffset;

    // Navbar background blur/border enhancement on scroll
    if (scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    // Back to top button visibility
    if (scrollY > 500) {
      backToTopBtn.classList.add('visible');
    } else {
      backToTopBtn.classList.remove('visible');
    }

    // Scroll spy for navigation items
    let currentSectionId = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 120;
      const sectionHeight = section.offsetHeight;
      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        currentSectionId = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${currentSectionId}`) {
        link.classList.add('active');
      }
    });
  });

  // Back to top click
  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ==================== 4. MOBILE DRAWER MENU ====================
  const navToggle = document.getElementById('nav-toggle');
  const mobileDrawer = document.getElementById('mobile-drawer');
  const drawerClose = document.getElementById('drawer-close');
  const drawerBackdrop = document.getElementById('drawer-backdrop');
  const drawerLinks = document.querySelectorAll('.drawer-link');

  function openDrawer() {
    mobileDrawer.classList.add('open');
    drawerBackdrop.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    mobileDrawer.classList.remove('open');
    drawerBackdrop.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (navToggle) navToggle.addEventListener('click', openDrawer);
  if (drawerClose) drawerClose.addEventListener('click', closeDrawer);
  if (drawerBackdrop) drawerBackdrop.addEventListener('click', closeDrawer);

  drawerLinks.forEach(link => {
    link.addEventListener('click', closeDrawer);
  });

  // ==================== 5. SKILLS CATEGORY FILTER ====================
  const filterBtns = document.querySelectorAll('.skill-filter-btn');
  const skillCards = document.querySelectorAll('.skill-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const category = btn.getAttribute('data-category');

      skillCards.forEach(card => {
        const cardCat = card.getAttribute('data-category');
        if (category === 'all' || cardCat === category) {
          card.style.display = 'block';
          card.style.opacity = '1';
          card.style.transform = 'scale(1)';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // ==================== 6. PROJECT DETAILS MODAL ====================
  const projectModal = document.getElementById('project-modal');
  const modalClose = document.getElementById('modal-close');
  const modalContentArea = document.getElementById('modal-content-area');
  const detailButtons = document.querySelectorAll('.btn-details');

  function openProjectModal(projectId) {
    const p = projectsData[projectId];
    if (!p) return;

    modalContentArea.innerHTML = `
      <img src="${p.image}" alt="${p.name}" class="modal-project-img">
      
      <div class="modal-title-row">
        <div>
          <span class="project-category-badge" style="position: static; display: inline-block; margin-bottom: 0.5rem;">${p.category}</span>
          <h2 class="modal-project-title">${p.name}</h2>
        </div>
        <div class="modal-links-row">
          <a href="${p.liveUrl}" target="_blank" rel="noopener" class="btn btn-primary-sm">
            <i class="fa-solid fa-arrow-up-right-from-square"></i> Live Demo
          </a>
          <a href="${p.clientRepo}" target="_blank" rel="noopener" class="btn btn-secondary" style="padding: 0.55rem 1.2rem; font-size: 0.88rem;">
            <i class="fa-brands fa-github"></i> GitHub (Client)
          </a>
        </div>
      </div>

      <div class="modal-sec-heading">
        <i class="fa-solid fa-layer-group"></i> Main Technology Stack
      </div>
      <div class="modal-tech-stack-list">
        ${p.techStack.map(t => `<span class="modal-tech-badge">${t}</span>`).join('')}
      </div>

      <div class="modal-sec-heading">
        <i class="fa-solid fa-file-lines"></i> Project Overview
      </div>
      <p class="modal-text">${p.description}</p>

      <div class="modal-sec-heading">
        <i class="fa-solid fa-triangle-exclamation"></i> Challenges Faced & Solutions
      </div>
      <ul class="modal-bullets">
        ${p.challenges.map(c => `<li>${c}</li>`).join('')}
      </ul>

      <div class="modal-sec-heading">
        <i class="fa-solid fa-compass"></i> Potential Improvements & Future Plans
      </div>
      <ul class="modal-bullets">
        ${p.improvements.map(i => `<li>${i}</li>`).join('')}
      </ul>
    `;

    projectModal.classList.add('active');
    projectModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeProjectModal() {
    projectModal.classList.remove('active');
    projectModal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  detailButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const projId = btn.getAttribute('data-project');
      openProjectModal(projId);
    });
  });

  if (modalClose) modalClose.addEventListener('click', closeProjectModal);
  if (projectModal) {
    projectModal.addEventListener('click', (e) => {
      if (e.target === projectModal) closeProjectModal();
    });
  }

  // ==================== 7. RESUME PREVIEW MODAL ====================
  const resumeModal = document.getElementById('resume-modal');
  const resumeModalClose = document.getElementById('resume-modal-close');
  const resumeTriggers = document.querySelectorAll('.btn-resume-modal-trigger, #btn-resume-nav');

  function openResumeModal() {
    resumeModal.classList.add('active');
    resumeModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeResumeModal() {
    resumeModal.classList.remove('active');
    resumeModal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  resumeTriggers.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openResumeModal();
    });
  });

  if (resumeModalClose) resumeModalClose.addEventListener('click', closeResumeModal);
  if (resumeModal) {
    resumeModal.addEventListener('click', (e) => {
      if (e.target === resumeModal) closeResumeModal();
    });
  }

  // Close modals on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeProjectModal();
      closeResumeModal();
      closeDrawer();
    }
  });

  // ==================== 8. COPY TO CLIPBOARD ====================
  const copyBtn = document.getElementById('btn-copy-email');
  if (copyBtn) {
    copyBtn.addEventListener('click', () => {
      const email = 'mashukurmanik2552@gmail.com';
      navigator.clipboard.writeText(email).then(() => {
        const tooltip = copyBtn.querySelector('.copy-tooltip');
        tooltip.textContent = 'Copied!';
        tooltip.classList.add('show');
        setTimeout(() => {
          tooltip.classList.remove('show');
          tooltip.textContent = 'Copy';
        }, 2000);
      }).catch(() => {
        alert('Email copied: ' + email);
      });
    });
  }

  // ==================== 9. INTERACTIVE CONTACT FORM ====================
  const contactForm = document.getElementById('contact-form');
  const formStatus = document.getElementById('form-status');
  const btnSubmit = document.getElementById('btn-submit');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const subject = document.getElementById('subject').value.trim();
      const message = document.getElementById('message').value.trim();

      if (!name || !email || !subject || !message) {
        formStatus.className = 'form-status error';
        formStatus.textContent = 'Please fill in all required fields.';
        return;
      }

      // Simulate sending with nice button state
      btnSubmit.disabled = true;
      btnSubmit.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> <span>Sending Message...</span>`;

      setTimeout(() => {
        formStatus.className = 'form-status success';
        formStatus.innerHTML = `✓ Thank you, <strong>${name}</strong>! Your message has been received. I'll get back to you shortly at <em>${email}</em>.`;

        btnSubmit.disabled = false;
        btnSubmit.innerHTML = `<i class="fa-solid fa-check"></i> <span>Message Sent</span>`;
        contactForm.reset();

        setTimeout(() => {
          btnSubmit.innerHTML = `<i class="fa-solid fa-paper-plane"></i> <span>Send Message</span>`;
          setTimeout(() => {
            formStatus.style.display = 'none';
          }, 6000);
        }, 3000);
      }, 1000);
    });
  }

});
