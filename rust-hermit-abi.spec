# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_with check
%global debug_package %{nil}

%global crate hermit-abi

Name:           rust-hermit-abi
Version:        0.4.0
Release:        1
Summary:        Hermit system calls definitions
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hermit-abi
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Hermit system calls definitions.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hermit-abi) = 0.4.0
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hermit-abi/default) = 0.4.0
Requires:       cargo
Requires:       crate(hermit-abi) = 0.4.0

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hermit-abi/alloc) = 0.4.0
Requires:       (crate(rustc-std-workspace-alloc/default) >= 1.0.0 with crate(rustc-std-workspace-alloc/default) < 2.0.0~)
Requires:       cargo
Requires:       crate(hermit-abi) = 0.4.0

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compiler_builtins-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hermit-abi/compiler_builtins) = 0.4.0
Requires:       (crate(compiler_builtins/default) >= 0.1.0 with crate(compiler_builtins/default) < 0.2.0~)
Requires:       cargo
Requires:       crate(hermit-abi) = 0.4.0

%description -n %{name}+compiler_builtins-devel %{_description}

This package contains library source intended for building other packages which
use the "compiler_builtins" feature of the "%{crate}" crate.

%files       -n %{name}+compiler_builtins-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+core-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hermit-abi/core) = 0.4.0
Requires:       (crate(rustc-std-workspace-core/default) >= 1.0.0 with crate(rustc-std-workspace-core/default) < 2.0.0~)
Requires:       cargo
Requires:       crate(hermit-abi) = 0.4.0

%description -n %{name}+core-devel %{_description}

This package contains library source intended for building other packages which
use the "core" feature of the "%{crate}" crate.

%files       -n %{name}+core-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(hermit-abi/rustc-dep-of-std) = 0.4.0
Requires:       (crate(compiler_builtins/default) >= 0.1.0 with crate(compiler_builtins/default) < 0.2.0~)
Requires:       (crate(compiler_builtins/rustc-dep-of-std) >= 0.1.0 with crate(compiler_builtins/rustc-dep-of-std) < 0.2.0~)
Requires:       cargo
Requires:       crate(hermit-abi) = 0.4.0
Requires:       crate(hermit-abi/alloc) = 0.4.0
Requires:       crate(hermit-abi/core) = 0.4.0

%description -n %{name}+rustc-dep-of-std-devel %{_description}

This package contains library source intended for building other packages which
use the "rustc-dep-of-std" feature of the "%{crate}" crate.

%files       -n %{name}+rustc-dep-of-std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
