
frozenInfraDir=platform/repo/server/uiInfrastructureFrozen
frozenUiBundlerDir=platform/repo/server/uiBundlerFrozen
uiPlatformDir=platform/platform/src/main/c3/platform/src/uiPlatform

if [[ -d platform/platform/src/main/c3/platform/src/uiInfrastructure ]];
then
   git mv platform/platform/src/main/c3/platform/src/uiInfrastructure ${uiPlatformDir}
   git mv ${uiPlatformDir}/uiLoader ${uiPlatformDir}/loaders

   git mv platform/platform/src/main/java/c3/platform/uiInfrastructure platform/platform/src/main/java/c3/platform/uiPlatform
   git mv platform/platform/src/main/java/c3/platform/uiPlatform/uiLoader platform/platform/src/main/java/c3/platform/uiPlatform/loaders

   git rm platform/platform/src/main/java/c3/platform/uiInfrastructure/uiLoader
fi

actionsDir=${uiPlatformDir}/actions
annotationsDir=${uiPlatformDir}/annotations
bundlerDir=${uiPlatformDir}/bundler
componentsDir=${uiPlatformDir}/components
reactDir=${uiPlatformDir}/react
routesDir=${uiPlatformDir}/routes

mkdir -p $actionsDir
mkdir -p $annotationsDir
mkdir -p $bundlerDir
mkdir -p $componentsDir
mkdir -p $reactDir
mkdir -p $routesDir

# Redux Action types
git mv $frozenInfraDir/src/ui/actions/UiSdlComponentActionPayload.c3typ $actionsDir
git mv $frozenInfraDir/src/ui/components/actions/UiSdlInitialRenderAction.c3typ $actionsDir
git mv $frozenInfraDir/src/ui/components/actions/UiSdlInitialRenderPayload.c3typ $actionsDir
git mv $frozenInfraDir/src/ui/components/actions/UiSdlRegisterTriggersAction.c3typ $actionsDir
git mv $frozenInfraDir/src/ui/components/actions/UiSdlRegisterTriggersPayload.c3typ $actionsDir

# Annotation types
# git mv $frozenInfraDir/src/ui/annotations/Ann.UiSdlActionCreator.c3typ $annotationsDir
# git mv $frozenInfraDir/src/ui/annotations/Ann.UiSdlReducer.c3typ $annotationsDir
# git mv $frozenInfraDir/src/ui/annotations/Ann.UiSdlEpic.c3typ $annotationsDir
# git mv $frozenInfraDir/src/ui/annotations/Ann.UiSdlDataSpec.c3typ $annotationsDir

# Metadata Bundler
git mv $frozenInfraDir/src/UiSdlMetadataBundler.c3typ $bundlerDir
git mv $frozenInfraDir/src/UiSdlMetadataBundler.js $bundlerDir
git mv $frozenUiBundlerDir/src/UiTagMetadataStore.c3typ $bundlerDir
git mv $frozenUiBundlerDir/src/UiTagMetadataStore.js $bundlerDir

# Component types
git mv $frozenInfraDir/src/ui/components/UiSdlComponent.c3typ $componentsDir
git mv $frozenInfraDir/src/ui/components/UiSdlComponent.js $componentsDir
git mv $frozenInfraDir/src/ui/components/UiSdlComponent.ts $componentsDir
git mv $frozenInfraDir/src/ui/components/UiSdlNoData.c3typ $componentsDir
git mv $frozenInfraDir/src/UiSdlComponentRef.c3typ $componentsDir

# React/Redux compatibility types
git mv $frozenInfraDir/src/ui/native/UiSdlComponentMetadataStore.c3typ $reactDir
git mv $frozenInfraDir/src/ui/native/UiSdlEntitiesStore.c3typ $reactDir
git mv $frozenInfraDir/src/ui/native/UiSdlImmutableJS.c3typ $reactDir
git mv $frozenInfraDir/src/ui/native/UiSdlMetadataEntries.c3typ $reactDir
git mv $frozenInfraDir/src/ui/native/UiSdlReduxAction.c3typ $reactDir
git mv $frozenInfraDir/src/ui/native/UiSdlReduxState.c3typ $reactDir

# Routing types
git mv $frozenInfraDir/src/UiSdlRoute.c3typ $routesDir
git mv $frozenInfraDir/src/UiSdlRoute.js $routesDir

# Loader types
git mv $frozenInfraDir/src/bundling/loaders/* ${uiPlatformDir}/loaders/
