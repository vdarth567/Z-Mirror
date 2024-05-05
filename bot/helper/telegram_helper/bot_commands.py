#!/usr/bin/env python3
from bot import CMD_SUFFIX


class _BotCommands:
    def __init__(self):
        self.StartCommand       = 'start'
        self.MirrorCommand      = [f'pmirror{CMD_SUFFIX}',    f'pm{CMD_SUFFIX}']
        self.QbMirrorCommand    = [f'pqbmirror{CMD_SUFFIX}',  f'pqbm{CMD_SUFFIX}']
        self.YtdlCommand        = [f'pytdl{CMD_SUFFIX}',      f'pyt{CMD_SUFFIX}']
        self.LeechCommand       = [f'pleech{CMD_SUFFIX}',     f'pl{CMD_SUFFIX}']
        self.QbLeechCommand     = [f'pqbleech{CMD_SUFFIX}',   f'pqbl{CMD_SUFFIX}']
        self.YtdlLeechCommand   = [f'pytdlleech{CMD_SUFFIX}', f'pytl{CMD_SUFFIX}']
        self.CancelAllCommand   = [f'pcancelall{CMD_SUFFIX}', 'cancelallbot']
        self.RestartCommand     = [f'prestart{CMD_SUFFIX}',   'restartall']
        self.StatusCommand      = [f'pstatus{CMD_SUFFIX}',    'sall']
        self.PingCommand        = [f'ping{CMD_SUFFIX}',      'p']
        self.StatsCommand       = [f'pstats{CMD_SUFFIX}',     's']
        self.CloneCommand       = f'clone{CMD_SUFFIX}'
        self.CountCommand       = f'count{CMD_SUFFIX}'
        self.DeleteCommand      = f'del{CMD_SUFFIX}'
        self.CancelMirror       = f'pabort{CMD_SUFFIX}'
        self.ListCommand        = f'list{CMD_SUFFIX}'
        self.SearchCommand      = f'search{CMD_SUFFIX}'
        self.UsersCommand       = f'users{CMD_SUFFIX}'
        self.AuthorizeCommand   = f'pauthorize{CMD_SUFFIX}'
        self.UnAuthorizeCommand = f'punauthorize{CMD_SUFFIX}'
        self.AddSudoCommand     = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand      = f'rmsudo{CMD_SUFFIX}'
        self.HelpCommand        = f'phelp{CMD_SUFFIX}'
        self.LogCommand         = f'plog{CMD_SUFFIX}'
        self.ShellCommand       = f'shell{CMD_SUFFIX}'
        self.EvalCommand        = f'eval{CMD_SUFFIX}'
        self.ExecCommand        = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand      = f'pbsetting{CMD_SUFFIX}'
        self.UserSetCommand     = f'pusetting{CMD_SUFFIX}'
        self.BtSelectCommand    = f'btsel{CMD_SUFFIX}'
        self.RssCommand         = f'rss{CMD_SUFFIX}'
        self.CategorySelect     = f'catsel{CMD_SUFFIX}'
        self.RmdbCommand        = f'rmdb{CMD_SUFFIX}'
        self.RmalltokensCommand = f'rmat{CMD_SUFFIX}'

BotCommands = _BotCommands()
