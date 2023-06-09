from keeper_secrets_manager_core.core import KSMCache


def test_default_cache_file_name(monkeypatch):
    monkeypatch.delenv("KSM_CACHE_DIR", raising=False)
    assert KSMCache.get_cache_file_name() == KSMCache.DEFAULT_CACHE_FILE_NAME


def test_ksm_cache_dir_env_var(monkeypatch, tmpdir):
    monkeypatch.setenv("KSM_CACHE_DIR", str(tmpdir))
    expected_path = tmpdir / KSMCache.DEFAULT_CACHE_FILE_NAME
    assert KSMCache.get_cache_file_name() == str(expected_path)
