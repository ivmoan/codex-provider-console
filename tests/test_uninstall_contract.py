import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class UninstallContractTests(unittest.TestCase):
    def test_uninstall_is_guided_and_preserves_data_by_default(self):
        source = (ROOT / "codex-panel").read_text(encoding="utf-8")
        self.assertIn("卸载控制台，保留 Codex 数据（推荐）", source)
        self.assertIn("REMOVE_CODEX=false", source)
        self.assertIn("docker compose --profile reverse-proxy down --remove-orphans", source)
        self.assertIn("project_images=$(docker compose images -q", source)
        self.assertIn("realpath -m", source)
        self.assertIn("pgrep -f '[c]odex app-server'", source)
        self.assertIn("确认停止进程并继续删除", source)
        self.assertIn("已确认无残留", source)
        self.assertIn('cd "$HOME"', source)
        self.assertIn('请使用部署用户', source)
        self.assertIn('无法安全确认 Codex 数据目录', source)
        self.assertIn('system_proxy_backend', source)
        self.assertIn('/etc/nginx/codex-provider-console-certs', source)
        self.assertIn('/etc/sudoers.d/codex-provider-console-nginx-deploy', source)
        self.assertIn("codex-panel-preserved", source) if "codex-panel-preserved" in source else self.assertIn(".codex-preserved-", source)

    def test_uninstall_requires_confirmation_before_moving_relative_data(self):
        source = (ROOT / "codex-panel").read_text(encoding="utf-8")
        self.assertLess(source.index("确认执行卸载"), source.index("检测到数据位于项目目录内"))

if __name__ == "__main__":
    unittest.main()
