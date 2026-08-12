# CocoLink Web-React (소아과 병원 적응 에피소드 웹)

발달지연·자폐스펙트럼 아동을 위한 4단계 소아과 병원 적응 인터랙티브 웹 체험 프로그램입니다.

---

## 🚀 개발 및 실행 방법

```bash
# web-react 디렉토리로 이동
cd web-react

# 패키지 설치 (처음 실행 시)
npm install

# 로컬 개발 서버 실행
npm run dev
```

---

## 🌐 GitHub Pages 배포 가이드

> **Q. `main` 브랜치에 푸시하면 자동으로 배포되나요?**
>
> **네! 이제 `main` 브랜치에 Push하면 자동으로 GitHub Pages에 배포됩니다.**
> 프로젝트에 GitHub Actions 자동 배포 워크플로우(`.github/workflows/deploy.yml`)가 설정되어 있습니다.

### 배포 방법 2가지

#### 1️⃣ 수동 배포 (터미널 명령어)
로컬에서 바로 빌드하여 `gh-pages` 브랜치로 업데이트할 때 사용합니다.
```bash
cd web-react
npm run deploy
```
* `npm run deploy`를 실행하면 `predeploy` 스크립트에 의해 자동으로 `npm run build`가 선행된 후 `gh-pages` 브랜치로 배포됩니다.

#### 2️⃣ 자동 배포 (GitHub Push)
`main` 브랜치에 코드를 푸시하면 GitHub Actions가 자동으로 `web-react` 프로젝트를 빌드하고 GitHub Pages에 반영합니다.
```bash
git add .
git commit -m "feat: 업데이트 내용"
git push origin main
```

---

## ⚙️ GitHub Pages 서비스 최초 설정 확인 (최초 1회)

GitHub 웹사이트에서 아래 설정이 되어 있는지 확인해 주세요:

1. GitHub 레포지토리의 **Settings** 탭 클릭
2. 좌측 메뉴에서 **Pages** 클릭
3. **Build and deployment** 섹션의 **Source** 확인:
   - **Branch**: `gh-pages` 선택 / `/ (root)` 선택 후 **Save** 버튼 클릭

---

## 🔗 배포 주소
- **GitHub Pages URL**: `https://bulkasari.github.io/cocolink/`
