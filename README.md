# CocoLink (코코링크)

발달지연·자폐스펙트럼 아동을 위한 소아과 병원 적응 인터랙티브 에피소드 프로젝트입니다.

## 📂 프로젝트 구조

- **`web-react/`**: React + Vite 기반의 인터랙티브 웹 체험 프로그램
- **`Docs/`**: 기획 및 사양 문서
- **`Movie/` & `Hospital/`**: 에피소드 비디오 및 자원 파일

---

## 🌐 GitHub Pages 배포 가이드

### Q. `main` 브랜치에 올리면 자동으로 배포되나요?
> **네! 이제 `main` 브랜치에 코드를 푸시하면 자동으로 GitHub Pages에 배포됩니다.**
> 레포지토리에 GitHub Actions 자동 배포 워크플로우(`.github/workflows/deploy.yml`)를 등록해 두었습니다.

### 배포 방법

#### 1. 자동 배포 (권장)
`main` 브랜치로 커밋 및 푸시하면 GitHub Actions가 자동으로 빌드 및 배포를 수행합니다.
```bash
git add .
git commit -m "feat: 업데이트"
git push origin main
```

#### 2. 수동 배포 (터미널)
터미널에서 직접 수동으로 빠르게 배포하고 싶을 때는 아래 명령어를 실행하세요.
```bash
cd web-react
npm run deploy
```

---

## ⚙️ GitHub Pages 설정 확인 (최초 1회)

GitHub 웹사이트의 저장소 페이지에서 설정 확인이 필요합니다:
1. 저장소 상단 **Settings** -> 좌측 **Pages** 이동
2. **Branch**: `gh-pages` / `/ (root)` 로 선택 후 **Save**

🔗 **배포 주소**: [https://bulkasari.github.io/cocolink/](https://bulkasari.github.io/cocolink/)
